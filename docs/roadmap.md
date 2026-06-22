# Roadmap

This roadmap describes planned project directions. It is not a promise of scope or timeline.

## Current alpha focus

The current repository focuses on:

- technical consistency checks
- reproducible recalculation
- neutral issue reporting
- synthetic case studies
- command-line usability
- responsible-use guidance

## Near-term priorities

| Priority | Area | Planned work |
|---|---|---|
| P0 | Reliability | Keep tests passing across supported Python versions |
| P0 | Documentation | Keep README, docs, and case studies aligned |
| P1 | CLI usability | Improve command output formatting and error messages |
| P1 | Scientific checks | Add more electrochemistry-specific consistency checks |
| P1 | Case studies | Add additional synthetic examples for common audit workflows |
| P2 | Documentation site | Improve GitHub Pages navigation and examples |
| P2 | Packaging | Prepare for possible PyPI publication after API stabilization |

## Candidate scientific checks

Possible future checks include:

- ASR/Rp component-sum consistency
- area normalization checks
- gas-flow and Faradaic-efficiency consistency
- electrolysis voltage, current, gas-production, and efficiency checks
- conductivity unit conversion checks
- activation-energy fitting with configurable conventions
- source-data/table/figure tolerance reports

## Scope boundaries

The project will continue to avoid:

- author-intent inference
- misconduct classification
- uploading copyrighted publisher PDFs
- embedding real paper data in examples unless the data are legally reusable and clearly cited

## Contribution direction

Contributions are most useful when they add:

1. one reproducible technical check
2. one synthetic example
3. one neutral reporting template
4. tests or documentation showing how to use the check
