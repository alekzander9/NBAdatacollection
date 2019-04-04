import requests

forbes_valuation_url = 'https://www.forbes.com/ajax/list/data?year=2018&uri=nba-valuations&type=organization'

r = requests.get(forbes_valuation_url)

if r.status_code:
    data = r.json()

print(data[0]["revenue"])