# Tech-Insight Interview

## Requirements
- Python 3.6+
- requests
- BeautifulSoup4
- tweepy
- google-cloud-core==0.29.1
- google-cloud-bigtable==0.32.1
- lxml parser

## Data sources
- Forbes
- ESPN
- Twitter

## Scripts
### CreateDB
Create Google Cloud BigTable table and schema

### buildDataset
Consolidate other datasets into the final dataset. Create new features as well.

Team dataset:
- team
- home_games
- home_total
- home_average
- home_percentage
- away_games
- away_average
- away_percentage
- games
- average
- percentage
- operatingIncome
- debtValue
- oneYearValueChange
- valueList
- revenue
- followers_count
- salary_mass
- total_players_followers_count
- average_players_followers_count
- total_players_follower_dollar_ratio
- average_players_follower_dollar_ratio
- year

Player dataset:
- player
- position
- team
- salary
- followers_count
- follower_dollar_ratio
- year

### GetPlayerSalary
Fetch players salary from 2000 to 2019

#### Columns
- player
- position
- team
- salary
- year

### GetTeamsAttendance
Fetch teams attendance from 2001 to 2019

#### Columns
- team
- home_games
- home_total
- home_average
- home_percentage
- away_games
- away_average
- away_percentage
- games
- average
- percentage
- year

### GetTeamsRevenues
Fetch teams revenues data from 2012 to 2019

#### Columns
- team
- operatingIncome
- debtValue
- oneYearValueChange
- valueList
- revenue
- year

### GetTwitterFollowerCount
Fetch number of followers for a list of accounts

#### Columns
- account
- followers_count
- verified