# Release Checklist

Use this checklist before publishing a GitHub release.

## 1. Repository state

- [ ] All intended pull requests are merged.
- [ ] `main` is up to date.
- [ ] GitHub Actions pass on `main`.
- [ ] README examples match the current CLI.
- [ ] Synthetic case studies are clearly marked as synthetic.
- [ ] No private data, copyrighted PDFs, real paper data, author names, or DOIs are unintentionally included.

## 2. Version metadata

- [ ] `pyproject.toml` version is correct.
- [ ] `src/paper_audit/__init__.py` version is correct.
- [ ] `CITATION.cff` version and release date are correct.
- [ ] `CHANGELOG.md` includes the release notes.
- [ ] `docs/releases/` includes a copy-ready release note for the target version.

## 3. Documentation

- [ ] `docs/index.md` is up to date.
- [ ] `docs/getting_started.md` still runs.
- [ ] `docs/workflows.md` matches the current CLI and methodology.
- [ ] `docs/case_studies.md` lists the current synthetic examples.
- [ ] `docs/responsible_use.md` reflects current contribution rules.

## 4. GitHub repository metadata

Recommended About description:

```text
Physics-informed data consistency and reproducibility audit framework for materials electrochemistry papers.
```

Recommended topics:

```text
reproducibility
research-integrity
post-publication-review
materials-science
electrochemistry
solid-oxide-cells
data-consistency
scientific-computing
```

## 5. Suggested release metadata

For the current consolidated alpha release:

```text
Tag: v0.10.0-alpha
Title: v0.10.0-alpha
Target: main
Pre-release: yes
Release notes: docs/releases/v0.10.0-alpha.md
```

## 6. Suggested release note template

```markdown
## Summary

This alpha release provides a physics-informed toolkit for technical consistency checks in materials electrochemistry papers.

## Highlights

- Installable `paper-audit` CLI
- Arrhenius, statistics, ratio, and dimensional checks
- Batch tolerance reports
- Rp/ASR component-sum checks
- Faradaic-efficiency checks
- Conductivity geometry-normalization checks
- Synthetic case studies
- PubPeer-style neutral reporting templates
- Responsible-use and contribution guidance
- GitHub Pages documentation foundation

## Responsible-use note

This project supports technical clarification and reproducibility-oriented review. It does not infer author intent or classify misconduct.
```
