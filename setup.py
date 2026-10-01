# Project metadata lives in pyproject.toml. This file only exists because
# scikit-build (classic) drives CMake through setup() and versioneer
# supplies the version through setup.py hooks.
import versioneer
from skbuild import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['castxml'],
    cmake_install_dir='castxml/data',
)
