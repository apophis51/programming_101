import requests

api_key = "56ed50c8a72b44c7bb812239aacf80ed"

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-11-10&sortBy=publishedAt&apiKey=56ed50c8a72b44c7bb812239aacf80ed"
request = requests.get(url)
#content = request.text
content = request.json()
print(content["articles"])