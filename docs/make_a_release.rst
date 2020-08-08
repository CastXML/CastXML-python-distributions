.. _making_a_release:

================
Making a release
================

A core developer should use the following steps to create a release `X.Y.Z` of
**CastXML-python-distributions** on `PyPI`_.

This is usually done after :ref:`updating_castxml_version`.

-------------
Prerequisites
-------------

* All CI tests are passing on `AppVeyor`_, `CircleCI`_ and `Travis CI`_.

* You have a `GPG signing key <https://help.github.com/articles/generating-a-new-gpg-key/>`_.

-------------------------
Documentation conventions
-------------------------

The commands reported below should be evaluated in the same terminal session.

Commands to evaluate starts with a dollar sign. For example::

  $ echo "Hello"
  Hello

means that ``echo "Hello"`` should be copied and evaluated in the terminal.


---------------------
`PyPI`_: Step-by-step
---------------------

1. Make sure that all CI tests are passing on `AppVeyor`_, `CircleCI`_ and `Travis CI`_.


2. Download the latest sources

  .. code::

    $ cd /tmp && \
      git clone git@github.com:CastXML/CastXML-python-distributions CastXML-python-distributions-release && \
      cd CastXML-python-distributions-release

3. List all tags sorted by version

  .. code::

    $ git fetch --tags && \
      git tag -l | sort -V


4. Choose the next release version number

  .. code::

    $ release=X.Y.Z

  .. warning::

      To ensure the packages are uploaded on `PyPI`_, tags must match this regular
      expression: ``^[0-9]+(\.[0-9]+)*(\.post[0-9]+)?$``.


5. In `README.md`, update `PyPI`_ download count after running ``pypistats overall CastXML``
   and commit the changes.

  .. code::

    $ git add README.rst && \
      git commit -m "README: Update download stats"

  ..  note::

    To learn more about `pypistats`, see https://pypi.org/project/pypistats/


6. Tag the release

  .. code::

    $ git tag --sign -m "CastXML-python-distributions ${release}" ${release} master

  .. warning::

      We recommend using a `GPG signing key <https://help.github.com/articles/generating-a-new-gpg-key/>`_
      to sign the tag.


7. Publish the release tag

  .. code::

    $ git push origin ${release}

  .. note:: This will trigger builds on each CI services and automatically upload the wheels \
            and source distribution on `PyPI`_.

8. Check the status of the builds on `AppVeyor`_, `CircleCI`_ and `Travis CI`_.

9. Once the builds are completed, check that the distributions are available on `PyPI`_.

10. Create a clean testing environment to test the installation

  .. code::

    $ pushd $(mktemp -d) && \
      mkvirtualenv CastXML-${release}-install-test && \
      pip install CastXML && \
      castxml --version

  .. note::

      If the ``mkvirtualenv`` command is not available, this means you do not have `virtualenvwrapper`_
      installed, in that case, you could either install it or directly use `virtualenv`_ or `venv`_.

11. Cleanup

  .. code::

    $ popd && \
      deactivate  && \
      rm -rf dist/* && \
      rmvirtualenv CastXML-${release}-install-test

12. Publish master branch

  .. code::

    $ git push origin master

.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/
.. _virtualenv: http://virtualenv.readthedocs.io
.. _venv: https://docs.python.org/3/library/venv.html


.. _AppVeyor: https://ci.appveyor.com/project/CastXML/CastXML-python-distributions/history
.. _CircleCI: https://circleci.com/gh/CastXML/CastXML-python-distributions
.. _Travis CI: https://travis-ci.org/github/CastXML/CastXML-python-distributions/pull_requests

.. _PyPI: https://pypi.org/project/CastXML
