import argparse
import sys
from ql.console import Console


class DefaultArgumentInput(argparse.Action):
    def __init__(self, *args, **kwargs):
        super(DefaultArgumentInput, self).__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = input('Please enter value for %s: ' % self.metavar)
            try:
                values = self.type(values)
            except ValueError:
                parser.error(
                    "argument %s: invalid %s value: '%s'" % (
                        self.metavar, self.type.__name__, values))
        setattr(namespace, self.dest, values)


def main():
    parser = argparse.ArgumentParser(
        description='Interface for line-up management in JFR Teamy')

    parser.add_argument('round', metavar='ROUND',
                        action=DefaultArgumentInput,
                        type=int, nargs='?',
                        help='round number')
    parser.add_argument('segment', metavar='SEGMENT',
                        action=DefaultArgumentInput,
                        type=int, nargs='?',
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
