import requests
from bs4 import BeautifulSoup
import re
import time

years = range(2001, 2020)
data = {}

f = open("nba_attendance_2001_2019.csv", "w+")
headers = "team;home_games;home_total;home_average;home_percentage;away_games;away_average;away_percentage;games;average;percentage;year\n"
f.write(headers)

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
        row_data = {
            "home": {},
            "away": {}
        }


        team = row.contents[1].string
        row_data['home']['games'] = row.contents[2].string
        row_data['home']['total'] = row.contents[3].string
        row_data['home']['average'] = row.contents[4].string
        row_data['home']['percentage'] = row.contents[5].string
        row_data['away']['games'] = row.contents[6].string
        row_data['away']['average'] = row.contents[7].string
        row_data['away']['percentage'] = row.contents[8].string
        games = row.contents[9].string
        average = row.contents[10].string
        percentage = row.contents[11].string

        row_str = f"{team};{row_data['home']['games']};{row_data['home']['total']};{row_data['home']['average']};{row_data['home']['percentage']};{row_data['away']['games']};{row_data['away']['average']};{row_data['away']['percentage']};{games};{average};{percentage};{year}\n"
        row_str = row_str.replace(",","")

        if int(row_data['home']['games']) > 5:
            f.write(row_str)

        yearly_data[row.contents[1].string] = row_data

    time.sleep(0.5) # To avoid querying too often
    
    data[year] = yearly_data