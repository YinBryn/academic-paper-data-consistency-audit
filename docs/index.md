# Academic Paper Data Consistency Audit

A physics-informed toolkit for checking whether published materials electrochemistry papers are internally consistent.

The project focuses on technical clarification, reproducibility, and evidence-claim alignment. It does not judge author intent and does not make ethical allegations.

## What you can do

- Recalculate activation energies from Arrhenius data.
- Recalculate means, standard deviations, and reported statistics.
- Check power-density consistency using `P = j × V`.
- Generate batch source-data/table tolerance reports.
- Check Rp/ASR component sums.
- Check Faradaic-efficiency and gas-production consistency.
- Check conductivity geometry normalization.
- Compare figure, table, Supplementary Information, and source-data values.
- Draft neutral single-issue technical comments.

## Quick command

```bash
paper-audit arrhenius \
  --temperature-c 800 750 700 \
  --resistance 0.022 0.053 0.103
```

## Main sections

- [Getting started](getting_started.md)
- [Audit workflows](workflows.md)
- [Synthetic case studies](case_studies.md)
- [Responsible use](responsible_use.md)
- [Roadmap](roadmap.md)
- [Release checklist](release_checklist.md)
- [Launch kit](launch_kit.md)

## Additional examples

Representative command outputs are available in `../examples/cli_output/`.

## Repository

<https://github.com/YinBryn/academic-paper-data-consistency-audit>
