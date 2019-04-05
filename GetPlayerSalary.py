import requests
from bs4 import BeautifulSoup
import re
import time

years = range(2000, 2020)
data = {}

i = 1
page = 1

f = open("nba_salaries_2000_2019.csv", "w+")
headers = "player;position;team;salary;year\n"
f.write(headers)

for year in years:
    page = 1
    collected = 1
    while collected > 0:

        print(f"Current year: {year}, Page: {page}")
        
        espn_attendance_url = f'http://www.espn.com/nba/salaries/_/year/{year}/page/{page}'

        r = requests.get(espn_attendance_url)

        if r.status_code != 200:
            print(f"Error! Status code: {r.status_code}")
            exit(0)

        htmldata = BeautifulSoup(r.text, 'lxml')

        yearly_data = {}
        collected = 0

        table = htmldata.find(id="my-players-table").div.contents[1].table
        header_rows = table.find("tr", class_="colhead")
        team_rows = table.find_all("tr", class_=re.compile("row"))
        for row in team_rows:
            row_data = {}

            row_data["player"] = row.contents[1].contents[0].string
            row_data["position"] = row.contents[1].contents[1].string[2:]
            row_data["team"] = row.contents[2].contents[0].string
            row_data["salary"] = row.contents[3].string[1:].replace(",","")
            f.write(f"{row_data['player']};{row_data['position']};{row_data['team']};{row_data['salary']};{year}\n")
            #print("Player: {}, Position: {}, Team: {}, Salary: {}, Page: {}".format(row_data["player"], row_data["position"], row_data["team"], row_data["salary"], page))

            yearly_data[row_data["player"]] = row_data

            #print(f"{i}/{458+415}")
            collected = collected + 1
            i = i + 1
            
        page = page + 1
        data[year] = yearly_data

    time.sleep(0.5) # To avoid querying too often

f.close()