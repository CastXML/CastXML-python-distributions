.. _updating_castxml_version:

============================
Updating the CastXML version
============================

A developer should use the following steps to update the version ``X.Y.Z``
of CastXML associated with the current CastXML python distributions.
Available CastXML archives can be found `here <https://data.kitware.com/#folder/57b5de948d777f10f2696370>`_.

First, build the artifacts which will be made available for download.

Update CastXML files
--------------------

Using the `CastXMLSuperbuild <https://github.com/CastXML/CastXMLSuperbuild>`_
repository, create a merge request which will use CI to automatically generate
the appropriate binary files for the new version.  The version selection is
controlled by the ``CastXML_GIT_TAG`` variable.

If necessary, update the ``LLVM`` and ``clang`` versions.  Both objects have
a ``<>_version`` and a ``<>_md5`` variable which need to be be updated at the
same time.

Once the CI has finished, view the "Details" of each task.  Follow the links
to view and download the archive files created by each task. After download,
extract the contents of the associated archive file.  The content of each ZIP
file will be uploaded in the next step.

Upload files to data.kitware.com
--------------------------------

To upload the files generated in the previous step, first create the folder for
the new version of CastXML within the CastXML archive.  This can be done, after
signing in to the instance, by clicking on the folder button in the upper right
corner.

**Note**: If the only option in the menu is *Download folder*, create an issue
in this repository asking for write permission to this folder.

Create a folder with the same name as the version of ``CastXML_GIT_TAG`` and
upload the files from the previous step.

Update links in current repository
----------------------------------
1. Install `girder-client`::

    $ pip install girder-client

2. Execute `scripts/update_castxml_version.py` command line tool with the desired
   ``X.Y.Z`` CastXML version available for download. For example::

    $ release=0.3.6
    $ python scripts/update_castxml_version.py ${release}

    Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370'
    Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370' - done
    Updating 'CastXMLUrls.cmake' with CastXML version 0.3.6
    Updating 'CastXMLUrls.cmake' with CastXML version 0.3.6 - done
    Updating README.md
    Updating README.md - done
    Updating docs/update_castxml_version.rst
    Updating docs/update_castxml_version.rst - done
    Updating tests/test_distribution.py
    Updating tests/test_distribution.py - done

   *Note*: Ensure that the ``Win32_binary`` variables still are set to the
   content of the ``Win64_binary`` variable.  It may be set to NULL.

3. Create a topic named `update-to-castxml-X.Y.Z` and commit the changes.
   For example::

    release=0.3.6
    git checkout -b update-to-castxml-${release}
    git add CastXMLUrls.cmake README.md docs/update_castxml_version.rst tests/test_distribution.py
    git commit -m "Update to CastXML ${release}"

4. Create a `Pull Request`.

5. If all CI tests are passing, merge the topic and consider `making a new
   release <https://github.com/CastXML/CastXML-python-distributions/blob/master/docs/make_a_release.rst>`_.