# Making a release

Releases are built and uploaded to [PyPI][pypi] by the [Build + Test workflow][ci]
(`.github/workflows/ci.yml`). Publishing a GitHub release starts the workflow,
which builds CastXML from source on every platform, builds and tests the wheels
and the sdist, then uploads them to PyPI using trusted publishing. Pushes and
pull requests run the same builds and tests but never upload anything.

Every build compiles LLVM/Clang, so a full CI run takes a few hours.

## Release branches

`master` is where development happens. Each CastXML minor version gets its own
release branch, `releases/X.Y`, cut from `master`, and every release in that
series is tagged on it. A fix needed in a released series lands on `master`
first and is then cherry-picked onto the release branch, so `master` never has
to be held back or rewound for a release.

CI runs on pushes and pull requests for `master` and every `releases/**` branch.

## Updating the CastXML version

Skip this section if the release doesn't change the CastXML version.

CastXML is built by the [CastXML superbuild][superbuild], which builds LLVM/Clang
and then CastXML. `CMakeLists.txt` pins two revisions:

- `CASTXML_GIT_TAG`: the CastXML release to build, e.g. `v0.8.0`.
- `CASTXML_SUPERBUILD_GIT_TAG`: the superbuild commit, which decides the
  LLVM/Clang version. The superbuild also pins its own CastXML revision;
  `PatchCastXMLSuperbuild.cmake` replaces it with `CASTXML_GIT_TAG`.

1. On a branch from `master` named `update-to-castxml-X.Y.Z`:

   - Set `CASTXML_GIT_TAG` in `CMakeLists.txt` to `vX.Y.Z`.
   - If the new CastXML needs a newer LLVM, set `CASTXML_SUPERBUILD_GIT_TAG`
     to a superbuild commit that builds it.
   - Update the CastXML version in `README.md`, and `expected_version` in
     `tests/test_distribution.py`.

2. Open a pull request against `master`, and merge it once CI passes.

If a new superbuild commit changes how it pins CastXML, the build stops with a
message from `PatchCastXMLSuperbuild.cmake`; update that script to match.

## Cutting the release

1. Choose the release version, and set the release branch it belongs to:

   ```bash
   release=X.Y.Z
   branch=releases/X.Y
   ```

   The git tag *is* the package version: setuptools-scm reads it at build time.
   Use the bare form `X.Y.Z` with no `v` prefix, matching the CastXML version.
   For a packaging-only fix to a version that's already on PyPI, use
   `X.Y.Z.postN`.

2. Get the release branch ready.

   - **First release of a new CastXML minor version:** create the release
     branch from `master` and push it:

     ```bash
     git fetch origin
     git checkout -b ${branch} origin/master
     git push origin ${branch}
     ```

   - **Patch release in an existing series:** backport each fix from `master`
     with a pull request into the release branch:

     ```bash
     git fetch origin
     git checkout -b backport-<topic> origin/${branch}
     git cherry-pick -x <commit-on-master>
     git push origin backport-<topic>
     ```

     Open the pull request against `${branch}`, and merge it once CI passes.

   Then make sure your local branch matches what CI tested:

   ```bash
   git checkout ${branch}
   git pull origin ${branch}
   ```

3. Tag the release on the release branch and push the tag:

   ```bash
   git tag --sign -m "CastXML-python-distributions ${release}" ${release} ${branch}
   git push origin ${release}
   ```

   Signing the tag with a [GPG key][gpg] is recommended. Pushing the tag on its
   own doesn't start a build.

   Tag the first release of a series on the commit the branch was cut from,
   before anything is backported. That commit is also on `master`, so
   development builds from `master` get versions after the new release.

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
  only runs after every build succeeds. Fix the problem on `master`, backport
  the fix to the release branch, delete the release and its tag, and start
  again from step 3:

  ```bash
  gh release delete ${release} --cleanup-tag --yes
  git tag -d ${release}
  ```

- **A broken release reached PyPI:** PyPI never accepts the same version twice,
  even after it's deleted. Fix the problem and release `X.Y.Z.post1` from the
  same release branch.

[pypi]: https://pypi.org/project/castxml
[ci]: https://github.com/CastXML/CastXML-python-distributions/actions/workflows/ci.yml
[superbuild]: https://github.com/CastXML/CastXMLSuperbuild
[gpg]: https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key
