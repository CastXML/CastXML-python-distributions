.. _updating_castxml_version:

============================
Updating the CastXML version
============================

A developer should use the following steps to update the version ``X.Y.Z``
of CastXML associated with the current CastXML python distributions.

Available CastXML archives can be found `here <https://data.kitware.com/#folder/57b5de948d777f10f2696370>`_.

1. Install `girder-client`::

    $ pip install girder-client

2. Execute `scripts/update_castxml_version.py` command line tool with the desired
   ``X.Y.Z`` CastXML version available for download. For example::

    $ release=0.4.2
    $ python scripts/update_castxml_version.py ${release}

    Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370'
    Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370' - done
    Updating 'CastXMLUrls.cmake' with CastXML version 0.4.2
    Updating 'CastXMLUrls.cmake' with CastXML version 0.4.2 - done
    Updating README.md
    Updating README.md - done
    Updating docs/update_castxml_version.rst
    Updating docs/update_castxml_version.rst - done
    Updating tests/test_distribution.py
    Updating tests/test_distribution.py - done

3. Create a topic named `update-to-castxml-X.Y.Z` and commit the changes.
   For example::

    release=0.4.2
    git checkout -b update-to-castxml-${release}
    git add CastXMLUrls.cmake README.md docs/update_castxml_version.rst tests/test_distribution.py
    git commit -m "Update to CastXML ${release}"

4. Create a `Pull Request`.

5. If all CI tests are passing, merge the topic and consider `making a new
   release <https://github.com/CastXML/CastXML-python-distributions/blob/master/docs/make_a_release.rst>`_.