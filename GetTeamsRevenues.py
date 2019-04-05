import requests
import time

years = range(2012, 2020)

f = open("nba_team_revenues.csv", "w+")
headers = "team;operatingIncome;debtValue;oneYearValueChange;valueList;revenue;year\n"
f.write(headers)

data = {}

for year in years:
    forbes_valuation_url = f'https://www.forbes.com/ajax/list/data?year={year}&uri=nba-valuations&type=organization'
    r = requests.get(forbes_valuation_url)

    if r.status_code != 200:
        print(f"Error! Status code: {r.status_code}")
        exit(0)

    yearly_data = {}

    for row in r.json():
        yearly_data[row["name"]] = {
            "operatingIncome": row["operatingIncome"],
            "debtValue": row["debtValue"],
            "oneYearValueChange": row["oneYearValueChange"],
            "valueList": row["valueList"],
            "revenue": row["revenue"],
        }

        row_str = row['name'] + ";" + ";".join(str(x) for x in yearly_data[row["name"]].values()) + f";{year}\n"
        f.write(row_str)

    time.sleep(0.5) # To avoid querying too often