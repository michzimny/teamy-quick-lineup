from .orm.utils import get_num_of_tables
from .lineup import Lineup
from .completer import Completer


class Console(object):

    def __init__(self, round, segment, table=None):
        self.round = round
        self.segment = segment
        self.start_from_table = table if table is not None else 1

    @property
    def tables(self):
        return [ i for i in range(self.start_from_table, get_num_of_tables() + 1) ]

    def run(self):
        for table in self.tables:
            try:
                self.process_table(table)
            except (EOFError, KeyboardInterrupt):
                break

    def process_table(self, table):
        lineup = self.get_lineup(table)
        print(lineup.info)
        print('')
        # Python 2.x workaround
        global input
        try:
            input = raw_input
        except NameError:
            pass # if raw_input is not defined (Python 3.x), ignore it
        for team in lineup.teams:
            Completer.install_new_completer(team.player_names)
            for pair in team.pairs:
                while True:
                    print(pair.info)
                    value = input("Player: ")
                    if not value:
                        print()
                        break
                    pair.set_player(value)

    def get_lineup(self, table):
        return Lineup(self.round, self.segment, table)
