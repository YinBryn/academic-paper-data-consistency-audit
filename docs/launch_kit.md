# v0.10.0-alpha Launch Kit

This document collects copy-ready material for publishing and sharing the `v0.10.0-alpha` release.

## 1. GitHub Release

Use the following settings:

```text
Tag: v0.10.0-alpha
Target: main
Title: v0.10.0-alpha
Pre-release: yes
```

Use `docs/releases/v0.10.0-alpha.md` as the release-note body.

## 2. GitHub About Description

```text
Physics-informed data consistency and reproducibility audit framework for materials electrochemistry papers.
```

## 3. GitHub Topics

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

## 4. GitHub Pages Setup

Repository settings:

```text
Settings → Pages → Build and deployment → Deploy from a branch
Branch: main
Folder: /docs
Save
```

After Pages builds, the documentation homepage should be `docs/index.md`.

## 5. Short Public Announcement

```text
I have released v0.10.0-alpha of Academic Paper Data Consistency Audit, a physics-informed toolkit for checking whether materials electrochemistry papers are internally consistent.

It includes an installable paper-audit CLI for Arrhenius recalculation, I–V–P consistency, Rp/ASR component sums, Faradaic-efficiency checks, conductivity geometry normalization, and batch source-data/table tolerance reports.

The project is designed for reproducible technical clarification, not for inferring author intent or making misconduct allegations. All examples are synthetic.
```

## 6. Longer Public Announcement

```text
I have released v0.10.0-alpha of Academic Paper Data Consistency Audit.

This project is a physics-informed toolkit for checking whether reported values in materials electrochemistry papers are internally consistent. It focuses on reproducible recalculation, source-data comparison, and evidence-claim alignment.

The current release includes an installable paper-audit CLI with commands for:

- Arrhenius fitting and activation-energy recalculation
- statistics recalculation
- performance-ratio checks
- I–V–P consistency
- batch reported-value/source-data tolerance reports
- Rp/ASR component-sum checks
- Faradaic-efficiency and gas-production checks
- conductivity geometry-normalization checks

The repository also includes synthetic case studies, representative CLI outputs, neutral PubPeer-style comment templates, and responsible-use guidance.

The purpose is technical clarification and reproducibility-oriented review. The project does not infer author intent and does not classify misconduct.
```

## 7. One-line Pitch

```text
A physics-informed CLI toolkit for reproducible data-consistency checks in materials electrochemistry papers.
```

## 8. Suggested Hashtags

```text
#OpenScience #Reproducibility #MaterialsScience #Electrochemistry #SolidOxideCells #ScientificComputing
```
