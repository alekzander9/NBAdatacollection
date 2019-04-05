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

# TODO fetch teams from other file
# TODO fetch teams screen_name
teams = [
    # "@nyknicks",
    # "@Lakers",
    # "@warriors",
    "@chicagobulls",
    "@celtics",
    "@BrooklynNets",
    "@HoustonRockets",
    "@dallasmavs",
    # "@LAClippers",
    # "@MiamiHEAT",
    # "@Raptors",
    # "@sixers",
    # "@spurs",
    # "@trailblazers",
    # "@SacramentoKings",
    # "@WashWizards",
    # "@Suns",
    # "@okcthunder",
    # "@utahjazz",
    # "@Pacers",
    # "@nuggets",
    # "@Bucks",
    # "@OrlandoMagic",
    # "@ATLHawks",
    # "@cavs",
    # "@DetroitPistons",
    # "@Timberwolves",
    # "@hornets",
    # "@PelicansNBA",
    # "@memgrizz"
]

for team in teams:
    query = f"{team} -filter:retweets"
    results = api.search(q="chicagobulls -filter:retweets", count=1)
    print(f"Team: {team}")
    print(results)
    print(results[0]._json["text"])
    with open("nbatweet.txt", "a+") as f:
        for r in results:
            f.write(json.dumps(r._json))
            print(r._json)
        f.close()
    print(results)