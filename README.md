# teamy-quick-lineup
Command-line interface for line-up management in JFR Teamy.

# Installation

Download the pre-built bundle from one of the releases, unpack it and run the EXE file.

# Configuration

MySQL settings can be set in config.json, in application's runtime directory. Config file is created on first run if not present.

# Usage

```
quick_lineup.exe [<round> <segment> [<start from table>]]
```

For instance, to process round 3, segment 2, starting from table 1 run:

```
quick_lineup.exe 3 2 1
```

If round or segment are missing, the script will ask for these values interactively.

The script will iterate pair by pair in each match. It presents the currently assigned players and let you confirm them - pressing ENTER without any input - or change - providing player names (press TAB to autocomplete).

# Build requirements

Prerequisites:

* Python 3 (on Windows <= 3.4 due to the availability of MySQL connector)
* pip
* Windows environment: MySQL connector from Oracle, unavailable via PIP - https://dev.mysql.com/downloads/connector/python/

```
pip install -r requirements-PLATFORM.txt
```

Where `PLATFORM` is either `windows` or `linux`.

In source form, the script may be invoked directly from Python interpreter:

```
python quick_lineup.py [<round> <segment> [<start from table>]]
```

# Build details

See: [BUILD.md](BUILD.md)
