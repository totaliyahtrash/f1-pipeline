import json

def get_top_10(results):
    top_10 = [t for t in results if t['Position'] is not None and t['Position'] <=10]
    return sorted(top_10, key = lambda x:x['Position'])


def get_constructor_standings(results):
    team_points = {}
    for driver in results:
        team = driver['TeamName']
        points = driver['Points']

        if team not in team_points:
            team_points[team] = 0
        team_points[team] += points

    return sorted(team_points.items(), key=lambda x:x[1], reverse=True)


def get_zero_scorers(results):
    return [d['FullName'] for d in results if d['Points'] == 0]

def get_dnfs(results):
    return [d['FullName'] for d in results if d['Status'] != 'Finished']

def get_driver_of_race(results):
    max_gap = 0
    driver_name = ''
    for driver in results:
        if driver['GridPosition'] is None or driver['Position'] is None:
            continue
        if driver['GridPosition'] - driver['Position'] > max_gap:
            max_gap = driver['GridPosition'] - driver['Position']
            driver_name = driver['FullName']

    return driver_name,max_gap

