# F1 Race Data Pipeline 

An end-to-end ETL data pipeline built in Python that extracts, transforms, 
and analyses Formula 1 race data from any season, any race.

## What it does

- **Extract** — Pulls live F1 race data using the FastF1 library
- **Transform** — Cleans raw data: type conversion, time formatting, field normalisation, DNF handling
- **Analyze** — Generates race insights: top 10, constructor standings, position gainers, DNFs
- **Report** — Auto-generates a formatted race summary saved to txt

## Results — 2024 Italian GP (Monza)
