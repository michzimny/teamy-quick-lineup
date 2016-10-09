from django.db import models


class Team(models.Model):

    class Meta:
        db_table = 'teams'

    name = models.CharField(db_column='fullname', max_length=50)


class Player(models.Model):

    class Meta:
        db_table = 'players'

    first_name = models.CharField(db_column='gname', max_length=30)
    last_name = models.CharField(db_column='sname', max_length=30)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='players', db_column='team')

    @property
    def info(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.team.name)


class Segment(models.Model):

    ''' This class has no single primary key, so not all standard ORM API will work. '''

    class Meta:
        db_table = 'segments'

    round = models.IntegerField(db_column='rnd', primary_key=True)
    segment = models.IntegerField(db_column='segment', primary_key=True)
    table = models.IntegerField(db_column='tabl', primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='+', db_column='homet')
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='+', db_column='visit')
    openN = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='openN')
    openS = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='openS')
    openE = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='openE')
    openW = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='openW')
    closeN = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='closeN')
    closeS = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='closeS')
    closeE = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='closeE')
    closeW = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='+', db_column='closeW')

    def update(self, **kwargs):
        affected = Segment.objects.filter(round=self.round, segment=self.segment, table=self.table).update(**kwargs)
        assert affected == 1
        for field, value in kwargs.items():
            setattr(self, field, value)
