# Project Announcement Draft

## Short version

I have started an open-source project: **Academic Paper Data Consistency Audit**.

It is a physics-informed toolkit for checking whether published materials electrochemistry papers are internally consistent. The focus is not on accusation or author intent. The goal is to make technical clarification, recalculation, and evidence-claim alignment more reproducible.

Repository:

<https://github.com/YinBryn/academic-paper-data-consistency-audit>

## Longer version

Many technical discussions in materials electrochemistry begin with small inconsistencies between the main text, figures, tables, Supplementary Information, and source data. These inconsistencies can matter because conclusions often depend on derived quantities such as activation energies, polarization resistances, current-density-normalized performance metrics, diffusion coefficients, or transport-model parameters.

**Academic Paper Data Consistency Audit** provides a structured, neutral workflow for checking these links before writing a technical comment, preparing peer-review feedback, or designing follow-up experiments.

The current alpha version includes:

- Arrhenius fitting and activation-energy recalculation
- Mean and standard-deviation recalculation
- Performance-ratio checks
- Dimensional and I-V-P consistency checks
- PubPeer-style single-issue reporting templates
- Neutral language guidance for technical clarification
- Synthetic demo data only; no real paper data are included

The project is especially aimed at materials electrochemistry, solid oxide cells, protonic ceramic cells, ionic transport studies, and related areas.

The core principle is simple:

> Technical concerns should be locatable, reproducible, neutrally worded, and separated from judgments about author intent.

Feedback, issues, and contributions are welcome.

## Suggested tags

`#OpenScience` `#Reproducibility` `#MaterialsScience` `#Electrochemistry` `#SolidOxideCells` `#ScientificComputing` `#PostPublicationReview`
