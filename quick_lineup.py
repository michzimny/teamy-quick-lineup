import sys
from ql.console import Console


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Give correct parameters: round, segment and (optionally) table')
        sys.exit(1)

    round = int(sys.argv[1])
    segment = int(sys.argv[2])
    if len(sys.argv) == 4:
        table = int(sys.argv[3])
    else:
        table = None

    try:
        Console(round, segment, table).run()
    except:
        print('ERROR: %s' % sys.exc_info()[1])


if __name__ == '__main__':
    main()
