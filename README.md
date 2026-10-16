
# Serena Williams Career Match Analysis

## Project Overview

This project analyzes Serena Williams' career tennis matches to examine how the age difference between Serena and her opponents changed throughout her career.

The project uses Python to download, clean, and visualize match data. Quarto is used to generate HTML and PDF reports, and a Makefile automates the workflow.

## Data Source

Data comes from Tennis Abstract:

https://www.tennisabstract.com/cgi-bin/wplayer-classic.cgi?p=SerenaWilliams&f=Acareerqq

The raw JavaScript data is downloaded from:

https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js

## Repository Structure

- `scripts/download.py`: Downloads the raw match data.
- `scripts/clean.py`: Cleans the data and calculates player ages.
- `scripts/plot.py`: Creates the scatterplot.
- `data/`: Contains raw and cleaned data.
- `outputs/`: Contains the visualization and reports.
- `report.qmd`: Quarto report source.
- `Makefile`: Automates the analysis.
- `environment.yml`: Lists the required software dependencies.

## Methodology

The raw match data is downloaded from Tennis Abstract and converted into a pandas DataFrame.

Serena Williams' age and her opponent's age are calculated using their dates of birth and the match date.

The age difference is calculated as:

Age Difference = Serena's Age - Opponent's Age

Match outcomes are classified as wins or losses.

Observations with missing values required for the visualization are excluded.

The resulting cleaned dataset contains 1,038 matches.

## Visualization

![Serena Williams Career Matches](outputs/serena_plot.png)

The scatterplot shows Serena Williams' age on the x-axis and the difference between her age and her opponent's age on the y-axis.

Blue points represent wins, while purple points represent losses.

The visualization shows that Serena increasingly competed against younger opponents as her career progressed.

## Reproducing the Analysis

First, create the Conda environment:

```bash
conda env create -f environment.yml
conda activate serena-analysis
```

PDF generation also requires a working LaTeX installation.

To run the entire analysis:

```bash
make all
```

This downloads the raw data, cleans the dataset, generates the visualization, and creates the HTML and PDF reports.

To remove generated files:

```bash
make clean
```

## Tools Used

- Python
- pandas
- matplotlib
- requests
- Quarto
- GNU Make
- Git and GitHub
# hw2-Serena-analysis
