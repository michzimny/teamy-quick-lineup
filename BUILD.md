Build instructions
==================

Prerequisites
-------------

Building `quick_lineup` relies on `pyinstaller`.

You can install `pyinstaller` via PIP:

```
pip install pyinstaller
```

Build
-----

To build the binary, simply use the provided [`.spec` file](quick_lineup.spec):

```
pyinstaller quick_lineup.spec
```

The binary is compiled in the `dist` directory, while `build` directory contains intermediate files for `pyinstaller`.

Known issues
------------

 * it's difficult to pin-point a specific version of `pyinstaller` which is free from all issues, as `pyinstaller` develops dynamically
 * [pyinstaller < 3, requires manual patch] building from non-ASCII paths may be problematic or result in binaries which refuse to run
 * [pyinstaller >= 3.2] in some specific configuration, the resulting binary may not run from a non-ASCII path (see: https://github.com/pyinstaller/pyinstaller/issues/1396)
 * [pyinstaller >= 3.1, < 3.2] fails to overwrite its own files in `build`, the directory needs to be clean before building
 * appending EXE version info is broken due to an upstream bug, in Python3 WinAPI bindings: (see: https://github.com/pyinstaller/pyinstaller/issues/1955)
 * which is affected, anyway, by some antivirus software (if you're getting "Permission denied [Errno 5]" on metadata write, that may be it)

Best bet is to use 3.1 and clear `build` manually between builds. 3.2 (3.2.1 in my case) works fine, but some users reported inability to run the compiled EXE (hi, Olo).
