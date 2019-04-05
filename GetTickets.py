import requests

url = "https://www.vividseats.com/nba-basketball/atlanta-hawks-tickets/hawks-vs-pacers-4-10-2805299.html"
url2 = "https://www.vividseats.com/rest/v2/web/listings/2805299"

r = requests.get(url)

jar = r.cookies

print(r.status_code)
print(r.text)
print(jar)

r2 = requests.get(url2, cookies=jar)
