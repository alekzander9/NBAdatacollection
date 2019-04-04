import requests
import tweepy
import json

consumer_token = "KPnuikOo4a1m2g9MSJErgDjJ0"
consumer_secret = "QTrqCxNdHiSZPpyOvBAGQPggbX3VUubh4ls1eGJ10GKXuKtnBm"
    
access_token = "1113187943785619461-PeFxwPM3YAsUv5TNVJLIqG9aqDCcIl"
access_token_secret = "jjqMMIE4u4JMQ2aFaP9wF5Ts0zlLEbghxQgYWQqgVtTZV"
    
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

teams = [
    "nyknicks",
    "Los Angeles Lakers",
    "Golden State Warriors",
    "Chicago Bulls",
    "Boston Celtics",
    "Brooklyn Nets",
    "Houston Rockets",
    "Dallas Mavericks",
    "Los Angeles Clippers",
    "Miami Heat",
    "Toronto Raptors",
    "Philadelphia 76ers",
    "San Antonio Spurs",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "Washington Wizards",
    "Phoenix Suns",
    "Oklahoma City Thunder",
    "Utah Jazz",
    "Indiana Pacers",
    "Denver Nuggets",
    "Milwaukee Bucks",
    "Orlando Magic",
    "Atlanta Hawks",
    "Cleveland Cavaliers",
    "Detroit Pistons",
    "Minnesota Timberwolves",
    "Charlotte Hornets",
    "New Orleans Pelicans",
    "Memphis Grizzlies",
]

for team in teams:
    results = api.search_users(team, count=5)
    print("Team : {}, Account : {}, Followers : {}, Verified : {}".format(results[0]._json["name"], results[0]._json["screen_name"], results[0]._json["followers_count"], results[0]._json["verified"]))

# nyknicks_followers = api.get_user(screen_name="nyknicks")
# print(nyknicks_followers._json["followers_count"])