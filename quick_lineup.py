import argparse
import sys
from ql.console import Console


def main():
    parser = argparse.ArgumentParser(
        description='Interface for line-up management in JFR Teamy')

    parser.add_argument('round', metavar='ROUND', type=int,
                        help='round number')
    parser.add_argument('segment', metavar='SEGMENT', type=int,
                        help='segment number')
    parser.add_argument('table', metavar='TABLE', type=int,
                        nargs='?', default=None,
                        help='table to start from')

    arguments = parser.parse_args()

    try:
        Console(arguments.round, arguments.segment, arguments.table).run()
    except:
        print('ERROR: %s' % sys.exc_info()[1])


if __name__ == '__main__':
    main()
