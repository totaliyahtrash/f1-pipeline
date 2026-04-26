import json
import os

def transform_race_results(raw_data):
    for data in raw_data:
        try:
            data['Position'] = int(data['Position'])
            data['Points'] = int(data['Points'])
            data['GridPosition'] = int(data['GridPosition'])
            data['Laps'] = int(data['Laps'])
        except(ValueError,TypeError):
            data['Position'] = None
            data['Points'] = None
            data['GridPosition'] = None
            data['Laps'] = None
        clean_time = str(data['Time'])
        clean_time = clean_time.split(' ')[-1]
        clean_time = clean_time.split('.')[0]

        data["Time"] = clean_time
        fields_to_remove = ['HeadshotUrl', 'DriverId', 'TeamId', 'BroadcastName', 'Q1', 'Q2', 'Q3']
        for fields in fields_to_remove:
            del data[fields]

    return raw_data




def save_cleaned_data(cleaned_data,filename):
    os.makedirs('data/cleaned/',exist_ok=True)
    with open(f'data/cleaned/{filename}','w') as f:
        json.dump(cleaned_data,f,indent=4)
