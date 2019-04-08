import requests
from bs4 import BeautifulSoup
import re
import time

years = range(2001, 2020)

team_names = {
    'Hawks':'Atlanta Hawks',
    'Celtics':'Boston Celtics',
    'Nets':'Brooklyn Nets',
    'Hornets':'Charlotte Hornets',
    'Bulls':'Chicago Bulls',
    'Cavaliers':'Cleveland Cavaliers',
    'Mavericks':'Dallas Mavericks',
    'Nuggets':'Denver Nuggets',
    'Pistons':'Detroit Pistons',
    'Warriors':'Golden State Warriors',
    'Rockets':'Houston Rockets',
    'Pacers':'Indiana Pacers',
    'Clippers':'Los Angeles Clippers',
    'Lakers':'Los Angeles Lakers',
    'Grizzlies':'Memphis Grizzlies',
    'Heat':'Miami Heat',
    'Bucks':'Milwaukee Bucks',
    'Timberwolves':'Minnesota Timberwolves',
    'Pelicans':'New Orleans Pelicans',
    'NY Knicks':'New York Knicks',
    'Thunder':'Oklahoma City Thunder',
    'Magic':'Orlando Magic',
    '76ers':'Philadelphia 76ers',
    'Suns':'Phoenix Suns',
    'Trail Blazers':'Portland Trail Blazers',
    'Kings':'Sacramento Kings',
    'Spurs':'San Antonio Spurs',
    'Raptors':'Toronto Raptors',
    'Jazz':'Utah Jazz',
    'Wizards':'Washington Wizards'
}

def getTeamsAttendanceDataset():
    print("Building teams attendances dataset")

    f = open("nba_attendance_2001_2019.csv", "w+")
    headers = "team;home_games;home_total;home_average;home_percentage;away_games;away_average;away_percentage;games;average;percentage;year\n"
    f.write(headers)
    
    data = {}

    for year in years:
        espn_attendance_url = f'http://www.espn.com/nba/attendance/_/year/{year}'

        r = requests.get(espn_attendance_url)

        if r.status_code != 200:
            print(f"Error! Status code: {r.status_code}")
            exit(0)

        htmldata = BeautifulSoup(r.text, 'lxml')

        yearly_data = {}

        table = htmldata.find(id="my-teams-table").div.div.table
        header_rows = table.find("tr", class_="colhead")
        team_rows = table.find_all("tr", class_=re.compile("row"))
        for row in team_rows:
            row_data = {}

            team = row.contents[1].string
            row_data['home_games'] = row.contents[2].string
            row_data['home_total'] = row.contents[3].string
            row_data['home_average'] = row.contents[4].string
            row_data['home_percentage'] = row.contents[5].string
            row_data['away_games'] = row.contents[6].string
            row_data['away_average'] = row.contents[7].string
            row_data['away_percentage'] = row.contents[8].string
            games = row.contents[9].string
            row_data['games'] = row.contents[9].string
            average = row.contents[10].string
            row_data['average'] = row.contents[10].string
            percentage = row.contents[11].string
            row_data['percentage'] = row.contents[11].string

            if int(row_data['home_games']) > 5:
                row_str = f"{team_names[team]};{row_data['home_games']};{row_data['home_total']};{row_data['home_average']};{row_data['home_percentage']};{row_data['away_games']};{row_data['away_average']};{row_data['away_percentage']};{games};{average};{percentage};{year}\n"
                row_str = row_str.replace(",","")
                f.write(row_str)
                yearly_data[team_names[team]] = row_data

        time.sleep(0.5) # To avoid querying too often
        
        data[year] = yearly_data
    return data

if __name__ == '__main__':
    getTeamsAttendanceDataset()