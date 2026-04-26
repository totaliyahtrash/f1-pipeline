# F1 Race Data Pipeline 

An end-to-end ETL data pipeline built in Python that extracts, transforms, 
and analyses Formula 1 race data from any season, any race.

## What it does

- **Extract** — Pulls live F1 race data using the FastF1 library
- **Transform** — Cleans raw data: type conversion, time formatting, field normalisation, DNF handling
- **Analyze** — Generates race insights: top 10, constructor standings, position gainers, DNFs
- **Report** — Auto-generates a formatted race summary saved to txt

## Results — 2024 Italian GP (Monza)

 Winner: Charles Leclerc — Ferrari — 25pts
 Oscar Piastri — McLaren — 18pts
 Lando Norris — McLaren — 16pts
 Constructor Standings:
 Ferrari — 37pts | McLaren — 34pts | Mercedes — 16pts
 Driver of the Race: Franco Colapinto — gained 6 positions on F1 debut

 ## Tech Stack

- Python 3.14
- FastF1 — F1 telemetry and race data library
- JSON — raw and cleaned data storage
- Modular ETL architecture

## Project Structure

\```
f1-pipeline/
│
├── pipeline/
│   ├── __init__.py
│   ├── extractor.py
│   ├── transformer.py
│   ├── analyzer.py
│   └── writer.py
│
├── data/
│   ├── raw/
│   │   └── race_results.json
│   └── cleaned/
│       └── Monza2024.json
│
├── reports/
│   └── summary.txt
│
├── main.py
├── requirements.txt
└── README.md
\```


## How to run

```bash
pip install fastf1
python main.py
```

Change the race and year in `main.py`:

```python
run_pipeline(2024, 'Monza')      # 2024 Italian GP
run_pipeline(2023, 'Silverstone') # 2023 British GP
run_pipeline(2025, 'Australia')   # 2025 Australian GP
```

Works for any race from 1950–2025.

## What I learned building this

- Modular pipeline architecture — each file has one job
- Real-world data cleaning — handling NaN, wrong types, messy time formats
- Error handling — DNF drivers don't crash the pipeline
- File I/O — raw → cleaned → report flow
- Working with a real sports data library (FastF1)

## Author

Dhruv | Aspiring Data Engineer  
github.com/syntaxdsamurai
