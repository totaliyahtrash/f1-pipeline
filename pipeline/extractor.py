import json
import os


import fastf1

def extract_race_results(year,race_name):
    session = fastf1.get_session(year,race_name,'R')
    session.load()
    session_to_dict = session.results.to_dict(orient='records')

    os.makedirs('data/raw',exist_ok=True)
    print(os.getcwd())

    with open("data/raw/race_results.json",'w') as f:
        json.dump(session_to_dict,f,indent=4,default=str)

    return session_to_dict
