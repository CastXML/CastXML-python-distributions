"""Command line executable allowing to update CastXMLUrls.cmake
 given a CMake version.
"""

import argparse
import contextlib
import os
import re
import textwrap

try:
    import girder_client
except ImportError:
    raise SystemExit(
        "girder_client not available: "
        "consider installing it running 'pip install girder-client'"
    )

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")


@contextlib.contextmanager
def _log(txt, verbose=True):
    if verbose:
        print(txt)
    yield
    if verbose:
        print("%s - done" % txt)


def get_archive_urls_and_shas(version, verbose=False):

    host_url = 'https://data.kitware.com'
    folder_id = '57b5de948d777f10f2696370'

    with _log("Collecting URLs and SHAs from '%s/#folder/%s'" % (host_url, folder_id)):

        api_url = '%s/api/v1' % host_url
        gc = girder_client.GirderClient(apiUrl=api_url)

        folders = gc.listFolder('57b5de948d777f10f2696370')
        archive_folder_ids = [folder['_id'] for folder in folders if folder['name'] == "v%s" % version]
        assert len(archive_folder_ids) == 1

        items = gc.listItem(archive_folder_ids[0])

        expected_files = {
            "castxml-linux.tar.gz":  "linux64_binary",
            "castxml-macosx.tar.gz": "macosx_binary",
            "castxml-windows.zip":   "win64_binary",
        }

        # Get download URL and SHA512 for each file
        urls_and_shas = {}
        for item in items:
            files = list(gc.listFile(item['_id']))
            assert len(files) == 1
            file_id = files[0]['_id']
            file = files[0]['name']
            sha = files[0]['sha512']
            url = '%s/file/%s/download' % (api_url, file_id)
            if file in expected_files:
                identifier = expected_files[file]
                urls_and_shas[identifier] = (url, sha)
                if verbose:
                    print("[%s]\n%s\n%s\n" % (identifier, url, sha))

        assert len(urls_and_shas) == len(expected_files)

        return urls_and_shas


def generate_cmake_variables(urls_and_shas):
    template_inputs = {}

    for var_prefix, urls_and_shas in urls_and_shas.items():
        template_inputs["%s_url" % var_prefix] = urls_and_shas[0]
        template_inputs["%s_sha512" % var_prefix] = urls_and_shas[1]

    cmake_variables = textwrap.dedent("""
      #-----------------------------------------------------------------------------
      # CastXML binaries

      set(linux32_binary_url    "NA")  # Linux 32-bit binaries not available
      set(linux32_binary_sha512 "NA")

      set(linux64_binary_url    "{linux64_binary_url}")
      set(linux64_binary_sha512 "{linux64_binary_sha512}")

      set(macosx_binary_url    "{macosx_binary_url}")
      set(macosx_binary_sha512 "{macosx_binary_sha512}")

      set(win64_binary_url    "{win64_binary_url}")
      set(win64_binary_sha512 "{win64_binary_sha512}")

      # See https://github.com/CastXML/CastXML-python-distributions/issues/5
      set(win32_binary_url    "${{win64_binary_url}}")
      set(win32_binary_sha512 "${{win64_binary_sha512}}")
    """).format(**template_inputs)

    return cmake_variables


def update_urls_script(version):
    content = generate_cmake_variables(
        get_archive_urls_and_shas(version))
    urls_filename = "CastXMLUrls.cmake"
    urls_filepath = os.path.join(ROOT_DIR, urls_filename)

    msg = "Updating '%s' with CastXML version %s" % (urls_filename, version)
    with _log(msg), open(urls_filepath, "w") as urls_file:
        urls_file.write(content)


def _update_file(filepath, regex, replacement, verbose=True):
    msg = "Updating %s" % os.path.relpath(filepath, ROOT_DIR)
    with _log(msg, verbose=verbose):
        pattern = re.compile(regex)
        with open(filepath, 'r') as doc_file:
            lines = doc_file.readlines()
            updated_content = []
            for line in lines:
                updated_content.append(
                    re.sub(pattern, replacement, line))
        with open(filepath, "w") as doc_file:
            doc_file.writelines(updated_content)


def update_docs(version):
    pattern = re.compile(r"CastXML \d\.\d\.\d")
    replacement = "CastXML %s" % version
    _update_file(
        os.path.join(ROOT_DIR, "README.md"),
        pattern, replacement)

    pattern = re.compile(r"\d\.\d\.\d")
    replacement = version
    _update_file(
        os.path.join(ROOT_DIR, "docs/update_castxml_version.rst"),
        pattern, replacement)


def update_tests(version):
    pattern = re.compile(r'expected_version = "\d.(\d)+.\d"')
    replacement = 'expected_version = "%s"' % version
    _update_file(os.path.join(
        ROOT_DIR, "tests/test_distribution.py"), pattern, replacement)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'version', metavar='CASTXML_VERSION', type=str,
        help='CastXML version of the form X.Y.Z'
    )
    parser.add_argument(
        '--collect-only', action='store_true',
        help='If specified, only display the archive URLs and associated hashsums'
    )
    args = parser.parse_args()
    if args.collect_only:
        get_archive_urls_and_shas(args.version, verbose=True)
    else:
        update_urls_script(args.version)
        update_docs(args.version)
        update_tests(args.version)


if __name__ == "__main__":
    main()
