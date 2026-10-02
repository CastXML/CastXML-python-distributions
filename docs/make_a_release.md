# Making a release

Releases are built and uploaded to [PyPI][pypi] by the [Build + Test workflow][ci]
(`.github/workflows/ci.yml`). Publishing a GitHub release starts the workflow,
which builds and tests the wheels and the sdist, then uploads them to PyPI using
trusted publishing. Pushes and pull requests run the same builds and tests but
never upload anything.

## Updating the CastXML version

Skip this section if the release doesn't change the CastXML version.

Available CastXML archives can be found
[here](https://data.kitware.com/#folder/57b5de948d777f10f2696370).

1. Install `girder-client`:

   ```bash
   pip install girder-client
   ```

2. Run `scripts/update_castxml_version.py` with the CastXML version `X.Y.Z` to
   package. For example:

   ```bash
   release=0.4.5
   python scripts/update_castxml_version.py ${release}
   ```

   It updates the archive URLs and checksums, the version in `README.md`, and
   the expected version in the tests:

   ```
   Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370'
   Collecting URLs and SHAs from 'https://data.kitware.com/#folder/57b5de948d777f10f2696370' - done
   Updating 'CastXMLUrls.cmake' with CastXML version 0.4.5
   Updating 'CastXMLUrls.cmake' with CastXML version 0.4.5 - done
   Updating README.md
   Updating README.md - done
   Updating tests/test_distribution.py
   Updating tests/test_distribution.py - done
   ```

3. Commit the changes on a branch named `update-to-castxml-X.Y.Z`:

   ```bash
   git checkout -b update-to-castxml-${release}
   git add CastXMLUrls.cmake README.md tests/test_distribution.py
   git commit -m "Update to CastXML ${release}"
   ```

4. Open a pull request, and merge it once CI passes.

## Cutting the release

1. Choose the release version.

   ```bash
   release=X.Y.Z
   ```

   The git tag *is* the package version: setuptools-scm reads it at build time.
   Use the bare form `X.Y.Z` with no `v` prefix. For a packaging-only fix to a
   version that's already on PyPI, use `X.Y.Z.postN`.

2. Make sure your local `master` matches what CI tested:

   ```bash
   git checkout master
   git pull origin master
   ```

3. Tag the release and push the tag:

   ```bash
   git tag --sign -m "CastXML-python-distributions ${release}" ${release} master
   git push origin ${release}
   ```

   Signing the tag with a [GPG key][gpg] is recommended. Pushing the tag on its
   own doesn't start a build.

4. Publish a GitHub release for the tag. This is what starts the release build:

   ```bash
   gh release create ${release} --verify-tag --title "CastXML-python-distributions ${release}" --generate-notes
   ```

   Alternatively, in the GitHub UI, go to **Releases → Draft a new release**,
   choose the tag, and click **Publish release**. Saving a draft doesn't start
   the workflow; only publishing does.

5. Follow the run in the repository's **Actions** tab, or with `gh run watch`.
   If the `pypi` environment requires reviewers, the `publish` job waits until
   you approve it with **Review deployments** on the run page.

6. Once the run finishes, check that the wheels and sdist are on [PyPI][pypi].

7. Test the installation in a clean environment:

   ```bash
   python -m venv /tmp/castxml-${release}-test
   /tmp/castxml-${release}-test/bin/pip install castxml==${release}
   /tmp/castxml-${release}-test/bin/castxml --version
   rm -rf /tmp/castxml-${release}-test
   ```

## If something goes wrong

- **The build or tests fail:** nothing was uploaded, because the `publish` job
  only runs after every build succeeds. Fix the problem on `master`, delete the
  release and its tag, and start again from step 2:

  ```bash
  gh release delete ${release} --cleanup-tag --yes
  git tag -d ${release}
  ```

- **A broken release reached PyPI:** PyPI never accepts the same version twice,
  even after it's deleted. Fix the problem and release `X.Y.Z.post1`.

[pypi]: https://pypi.org/project/castxml
[ci]: https://github.com/CastXML/CastXML-python-distributions/actions/workflows/ci.yml
[gpg]: https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key
