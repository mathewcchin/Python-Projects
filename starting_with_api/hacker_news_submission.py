import requests


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
result = r.json()

for item in sorted(result):
    print(item)
