import requests
import tweepy
import json
from time import sleep

consumer_token = "KPnuikOo4a1m2g9MSJErgDjJ0"
consumer_secret = "QTrqCxNdHiSZPpyOvBAGQPggbX3VUubh4ls1eGJ10GKXuKtnBm"
    
access_token = "1113187943785619461-PeFxwPM3YAsUv5TNVJLIqG9aqDCcIl"
access_token_secret = "jjqMMIE4u4JMQ2aFaP9wF5Ts0zlLEbghxQgYWQqgVtTZV"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

teams = [
    "New York Knicks",
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

players = ['Milos Teodosic', 'Marco Belinelli', 'Wesley Johnson', 'Josh Jackson', 'Jonathon Simmons', 'Montrezl Harrell', 'Ish Smith', 'Jaren Jackson Jr.', 'Brandon Ingram', 'Kristaps Porzingis', "De'Aaron Fox", 'Ben McLemore', 'Alex Abrines', 'Patrick Patterson', 'Jason Smith', 'Marcus Morris', 'Trae Young', 'Dwight Howard', 'DeMarcus Cousins', 'Alexis Ajinca', 'Thabo Sefolosha', 'Aron Baynes', 'Jaylen Brown', 'Patrick Beverley', 'Tony Parker', 'Mike Muscala', 'Alan Williams', 'Dirk Nowitzki', 'Kyle Singler', 'Jonathan Isaac', 'Mo Bamba', 'Anthony Tolliver', 'Willie Cauley-Stein', 'Dragan Bender', 'Lauri Markkanen', 'Lance Stephenson', 'Ed Davis', "Kyle O'Quinn", 'Wendell Carter Jr.', 'Justin Holiday', 'Alex Len', 'Mike Scott', 'Luc Mbah a Moute', 'Emmanuel Mudiay', 'Kris Dunn', 'Frank Ntilikina', 'Glenn Robinson III', 'Collin Sexton', 'Stanley Johnson', 'Buddy Hield', 'Dennis Smith Jr.', 'Kevin Knox', 'J.J. Barea', 'Nene Hilario', 'Zach Collins', 'Frank Kaminsky', 'Mikal Bridges', 'Michael Beasley', 'Jamal Murray', 'Rodney Hood', 'Jodie Meeks', 'Justise Winslow', 'Malik Monk', 'Myles Turner', 'Allonzo Trier', 'Brook Lopez', 'Shai Gilgeous-Alexander', 'Trey Lyles', 'Ekpe Udoh', 'Devin Booker', 'Luke Kennard', 'Cameron Payne', 'Troy Daniels', 'Kelly Oubre Jr.', 'Miles Bridges', 'Marquese Chriss', 'Tomas Satoransky', 'Bryn Forbes', 'Donovan Mitchell', 'Terry Rozier', 'Jerome Robinson', 'Yogi Ferrell', 'Elfrid Payton', 'Bam Adebayo', 'Jakob Poeltl', 'Michael Porter Jr.', 'Justin Jackson', 'Thon Maker', 'Seth Curry', 'Cedi Osman', 'Sam Dekker', 'Troy Brown Jr.', 'Justin Patton', 'Guerschon Yabusele', 'Domantas Sabonis', 'Jerian Grant', 'Delon Wright', 'D.J. Wilson', 'Zhaire Smith', 'Dario Saric', 'Taurean Prince', 'Justin Anderson', 'Manu Ginobili', 'Reggie Bullock', 'Bobby Portis', 'Dante Cunningham', 'Donte DiVincenzo', 'Rondae Hollis-Jefferson', 'Emeka Okafor', 'Kendrick Perkins', 'Tyus Jones', 'Jarell Martin', 'T.J. Leaf', 'Wayne Ellington', 'Lonnie Walker IV', 'John Collins', 'Denzel Valentine', 'Larry Nance Jr.', 'Kevin Huerter', 'Brandon Jennings', 'Harry Giles III', 'Darius Miller', 'Juan Hernangomez', 'Josh Okogie', 'Raul Neto', 'Terrance Ferguson', 'Grayson Allen', 'Sean Kilpatrick', 'OG Anunoby', 'Jarrett Allen', 'Corey Brewer', 'Torrey Craig', 'Chandler Hutchison', 'Ante Zizic', 'Shabazz Napier', 'Tyler Zeller', 'Aaron Holiday', 'Tyler Lydon', 'DeAndre Liggins', 'Trey Burke', 'Malik Beasley', 'Moritz Wagner', 'Anfernee Simons', 'Nerlens Noel', 'Caleb Swanigan', 'Furkan Korkmaz', 'Landry Shamet', 'Caris LeVert', 'Jonah Bolden', 'Kyle Kuzma', 'Tony Bradley', 'Derrick White', 'Spencer Dinwiddie', 'MarShon Brooks', 'Julyan Stone', 'Josh Hart', 'Robert Williams III', 'Jacob Evans', 'Pat Connaughton', "DeAndre' Bembry", 'Dzanan Musa', 'James Ennis III', 'Omari Spellman', 'Luke Kornet', 'Rodions Kurucs', 'T.J. McConnell', 'Richaun Holmes', 'Dwight Buycks', 'Malachi Richardson', 'Jahlil Okafor', 'Pascal Siakam', 'Willy Hernangomez', 'Georgios Papagiannis', 'Dejounte Murray', 'Skal Labissiere', 'Jake Layman', 'Deyonta Davis', 'Amir Johnson', 'Shelvin Mack', 'Omri Casspi', 'Jeff Green', 'Luol Deng', 'Jamal Crawford', 'Georges Niang', 'Vince Carter', 'Sviatoslav Mykhailiuk', 'Mitchell Robinson', 'Ivan Rabb', 'Tyler Dorsey', 'Dwayne Bacon', 'Dakari Johnson', 'Thomas Bryant', 'Khem Birch', "Royce O'Neale", 'David Stockton', 'Daniel Theis', 'Semi Ojeleye', 'Jabari Bird', 'Antonio Blakeney', 'Alfonzo McKinnie', 'Ben Moore', 'Tyrone Wallace', 'Monte Morris', 'Daniel Hamilton', 'Tyson Chandler', 'Shaquille Harrison', 'Elie Okobo', 'Jalen Brunson', 'Okaro White', 'Joakim Noah', 'Melvin Frazier Jr.', 'Eric Moreland', 'Nick Young', 'Isaac Bonga', "Devonte' Graham", "De'Anthony Melton", 'Ron Baker', 'Austin Rivers', 'Chasson Randle', 'Jevon Carter', 'Chimezie Metu', 'Hamidou Diallo', 'Gary Trent Jr.', 'Bruce Brown', 'Alize Johnson', 'Brad Wanamaker', 'Patrick McCaw', 'Kenneth Faried', 'Brandon Goodwin', 'Gary Clark', 'Bruno Caboclo', 'Wesley Matthews', 'Salah Mejri', 'Nik Stauskas', 'Jeremy Lin', 'Enes Kanter', 'John Jenkins', 'Chris Boucher', 'Malcolm Miller', 'Markieff Morris', 'Henry Ellenson', 'Pau Gasol', 'Andrew Bogut', 'Jaylen Adams', 'Danuel House Jr.', 'Jimmer Fredette', 'Tim Frazier', 'Dairis Bertans', 'Ray Spalding', 'Deonte Burton', 'Cameron Reynolds', 'Chris Chiozza', 'JaKarr Sampson', 'Donatas Motiejunas', 'Michael Carter-Williams', 'Greg Monroe', 'Jemerrio Jones', 'Isaac Humphries', 'BJ Johnson']

def getTwitterFollowerCountDataset(accounts=[]):
    print("Building follower count dataset")
    followers_counts = {}
    
    f = open("followers_count.csv", "w+")
    headers = "account;followers_count;verified\n"
    f.write(headers)

    for account in accounts:
        results = api.search_users(account, count=15)
        # print("Team : {}, Account : {}, Followers : {}, Verified : {}".format(results[0]._json["name"], results[0]._json["screen_name"], results[0]._json["followers_count"], results[0]._json["verified"]))
        if len(results) > 0:
            followers_counts[account] = {
                'name': account,
                'followers': results[0]._json['followers_count'],
                'verified': results[0]._json['verified']
            }
            f.write(f"{account};{results[0]._json['followers_count']};{results[0]._json['verified']}\n")
        sleep(0.5) # niceness
    
    return followers_counts

if __name__ == '__main__':
    getTwitterFollowerCountDataset(players)