import requests
from bs4 import BeautifulSoup
import re

years = [(2019, range(1, 12)),(2018, range(1, 13))]
data = {}

i = 1

for year, pages in years:
    for page in pages:
        espn_attendance_url = 'http://www.espn.com/nba/salaries/_/year/{}/page/{}'.format(year, page)

        r = requests.get(espn_attendance_url)

        if r.status_code != 200:
            print("Error! Status code: {r.status_code}")

        htmldata = BeautifulSoup(r.text, 'lxml')

        yearly_data = {}

        table = htmldata.find(id="my-players-table").div.contents[1].table
        header_rows = table.find("tr", class_="colhead")
        team_rows = table.find_all("tr", class_=re.compile("row"))
        for row in team_rows:
            row_data = {}

            row_data["player"] = row.contents[1].contents[0].string
            row_data["position"] = row.contents[1].contents[1].string[2:]
            row_data["team"] = row.contents[2].contents[0].string
            row_data["salary"] = row.contents[3].string[1:]
            print("Player: {}, Position: {}, Team: {}, Salary: {}, Page: {}".format(row_data["player"], row_data["position"], row_data["team"], row_data["salary"], page))

            yearly_data[row_data["player"]] = row_data

            print(f"{i}/{458+415}")
            i = i + 1
        
    data[year] = yearly_data