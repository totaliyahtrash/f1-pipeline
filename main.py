from pipeline.extractor import extract_race_results
from pipeline.transformer import transform_race_results,save_cleaned_data
from pipeline.analyzer import get_top_10, get_constructor_standings, get_zero_scorers, get_dnfs, get_driver_of_race
from pipeline.writer import write_summary

def run_pipeline(year,race_name):
    print(f"Starting pipeline for {year},{race_name}")
    raw_data = extract_race_results(year,race_name)

    cleaned_data = transform_race_results(raw_data)

    save_data = save_cleaned_data(cleaned_data,f'{race_name}{year}.json')

    top10 = get_top_10(cleaned_data)
    constructors = get_constructor_standings(cleaned_data)
    dnfs = get_dnfs(cleaned_data)
    zero_scorers = get_zero_scorers(cleaned_data)
    driver_of_race = get_driver_of_race(cleaned_data)

    write_summary(top10, constructors, zero_scorers, dnfs, driver_of_race, race_name)

    print('Executed')


run_pipeline(2024,'Monza')