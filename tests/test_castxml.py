
import pytest

import castxml

from . import push_argv


def _run(program, args):
    func = getattr(castxml, program)
    args = ["%s.py" % program] + args
    with push_argv(args), pytest.raises(SystemExit) as excinfo:
        func()
    assert 0 == excinfo.value.code


def test_castxml_module():
    _run("castxml", ["--version"])
