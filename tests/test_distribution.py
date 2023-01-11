
import os
import pytest

from path import Path

DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dist'))


def _check_castxml_install(virtualenv, tmpdir):
    expected_version = "0.5.0"

    for executable_name in ["castxml"]:
        output = virtualenv.run(
            "%s --version" % executable_name, capture=True).splitlines()[0]
        assert output == "%s version %s" % (executable_name, expected_version)


@pytest.mark.skipif(not Path(DIST_DIR).exists(), reason="dist directory does not exist")
def test_wheel(virtualenv, tmpdir):
    wheels = Path(DIST_DIR).files(match="*.whl")
    if not wheels:
        pytest.skip("no wheel available")
    assert len(wheels) == 1
    print(wheels)

    virtualenv.run("pip install --no-index %s" % wheels[0])

    _check_castxml_install(virtualenv, tmpdir)
