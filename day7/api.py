import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
req = requests.get(url)

print(req.status_code)

data = req.json()
data_dict = data.items()
print(data.keys())
print(data["items"][0])