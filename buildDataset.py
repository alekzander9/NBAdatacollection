from GetPlayerSalary import getPlayerSalaryDataset
from GetTeamsAttendance import getTeamsAttendanceDataset
from GetTeamsRevenues import getTeamsRevenuesDataset
from GetTwitterFollowerCount import getTwitterFollowerCountDataset

teams_dataset = []

t_dataset_file = open("nba_teams_dataset.csv", "w+")
p_dataset_file = open("nba_players_dataset.csv", "w+")

teams_dataset_headers = [
    'team',
    'operatingIncome',
    'debtValue',
    'oneYearValueChange',
    'valueList',
    'revenue',
    'home_games',
    'home_total',
    'home_average',
    'home_percentage',
    'away_games',
    'away_average',
    'away_percentage',
    'followers_count',
    'salary_mass',
    'total_players_followers_count',
    'average_players_followers_count',
    'total_players_follower_dollar_ratio',
    'average_players_follower_dollar_ratio',
    'year'
]

players_dataset_headers = [
    'player',
    'position',
    'team',
    'salary',
    'followers_count',
    'follower_dollar_ratio',
    'year'
]

t_dataset_file.write(";".join(teams_dataset_headers) + "\n")
p_dataset_file.write(";".join(players_dataset_headers) + "\n")

years = range(2001, 2020)

revenues_dataset = getTeamsRevenuesDataset()
teams = list(revenues_dataset[2019].keys())
attendance_dataset = getTeamsAttendanceDataset()
players_salary_dataset = getPlayerSalaryDataset()
players = list([p_info['player'] for p_info in players_salary_dataset[2019]])
followers_count = getTwitterFollowerCountDataset(teams + players)

for p_info in players_salary_dataset[2019]:
    player = p_info['player']
    if player in followers_count and followers_count[player]['verified'] == True:
        p_info['followers_count'] = followers_count[player]['followers']
        p_info['follower_dollar_ratio'] = p_info['followers_count'] / p_info['salary']
    else:
        p_info['followers_count'] = 0
        p_info['follower_dollar_ratio'] = 0
    p_info['year'] = 2019

    row_str = ""
    for header in players_dataset_headers:  # Ensures matching feature order with header
        row_str = row_str + str(p_info[header]) + ";"
    row_str = row_str[:-1]
    p_dataset_file.write(row_str)

for p_info in players_salary_dataset[2018]:
    player = p_info['player']
    if player in followers_count and followers_count[player]['verified'] == True:
        p_info['followers_count'] = followers_count[player]['followers']
        p_info['follower_dollar_ratio'] = p_info['followers_count'] / p_info['salary']
    else:
        p_info['followers_count'] = 0
        p_info['follower_dollar_ratio'] = 0
    p_info['year'] = 2018

    row_str = ""
    for header in players_dataset_headers:  # Ensures matching feature order with header
        row_str = row_str + str(p_info[header]) + ";"
    row_str = row_str[:-1]
    p_dataset_file.write(row_str)

for team in teams:
    for year in years:
        revenues = revenues_dataset[year][team] if year in revenues_dataset and team in revenues_dataset[year] else None
        attendance = attendance_dataset[year][team] if year in attendance_dataset and team in attendance_dataset[year] else None
        team_data = {}
        if revenues:
            team_data = {**revenues}
        if attendance:
            team_data = {**team_data, **attendance}
        team_data["year"] = year

        if year in [2019, 2018]:
            team_data["followers_count"] = followers_count[team]["followers"]
        else:
            team_data["followers_count"] = 0

        if year in players_salary_dataset:
            salaries = players_salary_dataset[year]

            salary_mass = sum([p_info['salary'] for p_info in salaries if p_info['team'] == team])
            team_data["salary_mass"] = salary_mass

            if year in [2019, 2018]:
                players_from_team = [p_info['player'] for p_info in salaries if p_info['team'] == team]

                players_followers_count = [account_data["followers"] for account_data in followers_count.values() if account_data["verified"] == True and account_data["name"] in players_from_team]
                total_players_followers_count = sum(players_followers_count)
                average_players_followers_count = sum(players_followers_count) / len(players_from_team)

                team_data["total_players_followers_count"] = total_players_followers_count
                team_data["average_players_followers_count"] = average_players_followers_count

                players_follower_dollar_ratio = [p_info['follower_dollar_ratio'] for p_info in salaries if p_info['team'] == team]
                total_players_follower_dollar_ratio = sum(players_follower_dollar_ratio)
                average_players_follower_dollar_ratio = sum(players_follower_dollar_ratio) / len(players_from_team)

                team_data["total_players_follower_dollar_ratio"] = total_players_follower_dollar_ratio
                team_data["average_players_follower_dollar_ratio"] = average_players_follower_dollar_ratio

        teams_dataset.append(team_data)

        row_str = ""
        for header in teams_dataset_headers:  # Ensures matching feature order with header
            if header == 'team':
                continue
            if header not in team_data:
                print(f"Error - Team: {team}, Header: {header}, Year: {year}")
                continue
            row_str = row_str + ";" + str(team_data[header])
        t_dataset_file.write(team + row_str + "\n")

t_dataset_file.close()
p_dataset_file.close()