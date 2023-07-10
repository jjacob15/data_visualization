import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url) #pass the endpoint with headers if you need to them 
print(r.json()) #use the json function to extract the response in json
