import os
import subprocess
import sys

from ._version import __version__  # noqa: F401

DATA = os.path.join(os.path.dirname(__file__), 'data')

# In an editable install (pip install -e .) this file runs from the source
# tree, but the CMake-installed files live in site-packages. scikit-build-core
# adds that location to the package's __path__, so look there too.
for _path in __path__:
    if os.path.isdir(os.path.join(_path, 'data')):
        DATA = os.path.join(_path, 'data')
        break

BIN_DIR = os.path.join(DATA, 'bin')


def _program(name, args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + args)


def castxml():
    raise SystemExit(_program('castxml', sys.argv[1:]))
