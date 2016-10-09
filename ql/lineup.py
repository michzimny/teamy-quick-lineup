# -*- coding: utf-8 -*-
from django.utils.functional import cached_property
from .orm.models import Segment, Team, Player


class TeamInSegment(object):

    OPEN_NS = 'open NS'
    OPEN_EW = 'open EW'
    CLOSED_NS = 'closed NS'
    CLOSED_EW = 'closed EW'

    def __init__(self, team, segment):
        self.team = team
        self.segment = segment

    def get_paired_players_fields(self):
        raise NotImplementedError()

    @property
    def name(self):
        return self.team.name

    @property
    def players(self):
        return self.team.players

    @property
    def pairs(self):
        for players_fields_entity in self.get_paired_players_fields():
            yield Pair(self, players_fields_entity['fields'], players_fields_entity['label'])

    @property
    def player_names(self):
        return [ '%s %s' % (p.last_name, p.first_name) for p in self.team.players.order_by('last_name', 'first_name').all() ]


class HomeTeamInSegment(TeamInSegment):

    def __init__(self, *args, **kwargs):
        super(HomeTeamInSegment, self).__init__(*args, **kwargs)

    def get_paired_players_fields(self):
        return [
            {
                'fields': ['openN', 'openS'],
                'label': self.OPEN_NS,
            },
            {
                'fields': [ 'closeE', 'closeW' ],
                'label': self.CLOSED_EW,
            },
        ]


class AwayTeamInSegment(TeamInSegment):

    def __init__(self, *args, **kwargs):
        super(AwayTeamInSegment, self).__init__(*args, **kwargs)

    def get_paired_players_fields(self):
        return [
            {
                'fields': ['openE', 'openW' ],
                'label': self.OPEN_EW,
            },
            {
                'fields': [ 'closeN', 'closeS' ],
                'label': self.CLOSED_NS,
            },
        ]


class Pair(object):

    def __init__(self, team, players_fields, label):
        assert len(players_fields) == 2
        self.team = team
        self.players_fields = players_fields
        self.label = label
        self.last_changed_player_num = None

    @property
    def players(self):
        return [ self._load_player(field) for field in self.players_fields ]

    def _load_player(self, player_field):
        try:
            return getattr(self.team.segment, player_field)
        except Player.DoesNotExist:
            return None

    @property
    def info(self):
        return 'Team: %s - %s - %s' % (
            self.team.name,
            self.label,
            [ p.info if p is not None else '<blank>' for p in self.players ]
        )

    def set_player(self, name):
        try:
            last_name, first_name = name.split(' ')
            player = self.team.players.get(first_name=first_name, last_name=last_name)
        except (ValueError, Player.DoesNotExist):
            player = None

        if not player:
            print('Unknown player: %s' % name)
        else:
            player_to_be_changed_num = self._deduce_player_to_be_changed()
            print('changing %s to %s ' % (self.players[player_to_be_changed_num], player))

            field_name = self.players_fields[player_to_be_changed_num]
            self.team.segment.update(**{field_name: player})

            self.last_changed_player_num = player_to_be_changed_num

    def _deduce_player_to_be_changed(self):
        if self.players[0] is None:
            return 0
        if self.players[1] is None:
            return 1
        if self.last_changed_player_num is None:
            return 0  # cannot make reasonable decision
        else:
            return 1 - self.last_changed_player_num  # return the other player num


class Lineup(object):

    def __init__(self, round, segment, table):
        self.round = round
        self.segment = segment
        self.table = table

    @property
    def info(self):
        return 'Round %s, Segment %s, Table %s: %s vs %s' % \
                (self.round, self.segment, self.table, self.segment_obj.home_team.name, self.segment_obj.away_team.name)

    @cached_property
    def segment_obj(self):
        return Segment.objects.get(round=self.round, segment=self.segment, table=self.table)

    @property
    def teams(self):
        return [
            HomeTeamInSegment(self.segment_obj.home_team, self.segment_obj),
            AwayTeamInSegment(self.segment_obj.away_team, self.segment_obj),
        ]
