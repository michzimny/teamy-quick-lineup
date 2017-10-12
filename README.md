# teamy-quick-lineup
Command-line interface for line-up management in JFR Teamy.

# Installation

Prerequisites:

* Python 3 (on Windows <= 3.4 due to the availability of MySQL connector)
* pip
* Windows environment: MySQL connector from Oracle, unavailable via PIP - https://dev.mysql.com/downloads/connector/python/

```
pip install -r requirements-PLATFORM.txt
```

Where `PLATFORM` is either `windows` or `linux`.

You can also download the pre-built EXE release.

# Configuration

Set MySQL settings in config.json.

# Usage

```
python quick_lineup.py [<round> <segment> [<start from table>]]
```

For instance, to process round 3, segment 2, starting from table 1 run:

```
python quick_lineup.py 3 2 1
```

If round and segment are missing, the script will ask for these values interactively.

The script will iterate pair by pair in each match. It presents the currently assigned players and let you confirm them - pressing ENTER without any input - or change - providing player names (press TAB to autocomplete).

# Build process

See: [BUILD.md](BUILD.md)
