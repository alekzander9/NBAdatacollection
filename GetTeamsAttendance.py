import requests
from bs4 import BeautifulSoup
import re

years = [2019,2018]
data = {}

for year in years:
    espn_attendance_url = 'http://www.espn.com/nba/attendance/_/year/{}'.format(year)

    r = requests.get(espn_attendance_url)

    if r.status_code != 200:
        print("Error! Status code: {r.status_code}")

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

        row_data["home"]["games"] = row.contents[2].string
        row_data["home"]["total"] = row.contents[3].string
        row_data["home"]["average"] = row.contents[4].string
        row_data["home"]["percentage"] = row.contents[5].string
        row_data["away"]["games"] = row.contents[6].string
        row_data["away"]["average"] = row.contents[7].string
        row_data["away"]["percentage"] = row.contents[8].string

        yearly_data[row.contents[1].string] = row_data
    
    data[year] = yearly_data

print(data[2018]["Pacers"])
print(data[2019]["Pacers"])