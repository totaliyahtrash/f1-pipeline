import os

def write_summary(top10, constructors, zero_scorers, dnfs, driver_of_race, race_name):
    os.makedirs('reports/',exist_ok=True)
    with open('reports/summary.txt','w') as f:
        f.write('F1 Race Report\n')
        f.write(f'Race - {race_name}\n')
        f.write('___________________________\n')

        f.write('\n')
        f.write('Top 10 finishes')
        for driver in top10:
            f.write(f'{driver['Position']} - {driver['FullName']} - {driver['Points']} - {driver['TeamName']}\n')

        f.write('\n')
        f.write('Team Standings\n')
        for teams,points in constructors:
            f.write(f'{teams} - {points}pts\n')

        f.write('\n')
        f.write('Drivers who scored 0 pts\n')
        for driver in zero_scorers:
            f.write(f'{driver}\n')

        f.write('\n')
        f.write('Drivers who got dnfs\n')
        for driver in dnfs:
            f.write(f'{driver}\n')

        f.write('\n')
        name,gained = driver_of_race
        f.write(f'Driver of the race {name}, Positions gained - {gained}\n')

        f.write('___________________________\n')
