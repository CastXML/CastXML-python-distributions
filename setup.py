
import sys
import versioneer

from distutils.text_file import TextFile
from skbuild import setup


with open('README.md', 'r') as fp:
    readme = fp.read()


def parse_requirements(filename):
    with open(filename, 'r') as file:
        return TextFile(filename, file).readlines()


requirements = []
dev_requirements = parse_requirements('requirements-dev.txt')

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name='castxml',

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    author='Kitware',
    author_email='kitware@kitware.com',

    packages=['castxml'],

    cmake_install_dir='castxml/data',

    entry_points={
        'console_scripts': [
            'castxml=castxml:castxml'
        ]
    },

    url=r'https://github.com/CastXML/CastXML#readme',
    download_url='',
    project_urls={
        "Bug Tracker": "https://github.com/CastXML/CastXML-python-distributions/issues",
        "Documentation": "https://github.com/CastXML/CastXML/blob/master/doc/manual/castxml.1.rst#castxml1",
        "Source Code": "https://github.com/CastXML/CastXML-python-distributions"
    },

    description=r'Parse C-family source files and optionally write a subset of '
                r'the Abstract Syntax Tree (AST) to a representation in XML.',

    long_description=readme,
    long_description_content_type='text/markdown',

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
        ],

    license='Apache 2.0',

    keywords='ast xml CMake build c++ cross-platform',

    install_requires=requirements,
    tests_require=dev_requirements,
    setup_requires=setup_requires
    )
