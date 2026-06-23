# Public Project Checklist

Use this checklist before and after a public release.

## Repository page

- [ ] The About description is concise and accurate.
- [ ] Topics match the project scope.
- [ ] The README starts with a clear one-sentence value proposition.
- [ ] The Quick Start section can be followed by a new user.
- [ ] The command examples use synthetic values.
- [ ] The project scope is clearly bounded.

## Documentation site

- [ ] GitHub Pages is enabled.
- [ ] The documentation homepage loads correctly.
- [ ] Navigation links work.
- [ ] The getting-started page includes `paper-audit demo`.
- [ ] The workflow tutorial shows an end-to-end path.
- [ ] Expected CLI output fields are documented.

## Release page

- [ ] The tag matches the package version.
- [ ] The release title matches the tag.
- [ ] Alpha releases are marked as pre-releases.
- [ ] The release notes describe the current scope.
- [ ] The release notes link back to the documentation.

## Install and run

- [ ] Fresh clone succeeds.
- [ ] Virtual environment creation succeeds.
- [ ] `pip install -r requirements.txt` succeeds.
- [ ] `pip install -e .` succeeds.
- [ ] `paper-audit --help` succeeds.
- [ ] `paper-audit demo` succeeds.
- [ ] `pytest tests/` succeeds.

## Content review

- [ ] Public examples are synthetic.
- [ ] Comments and templates are neutral and technical.
- [ ] The documentation separates observation, recalculation, and interpretation.
- [ ] The repository does not depend on local machine paths.
- [ ] The repository does not require unpublished datasets for examples.

## After release

- [ ] Create or update a post-release hardening issue.
- [ ] Check that GitHub Actions passes after merge.
- [ ] Check that the documentation site rebuilds.
- [ ] Check the README rendering on the public repository page.
- [ ] Decide the next small usability improvement.
