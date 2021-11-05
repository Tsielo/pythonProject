import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lon":"38.5","lat":"-78.5"}

headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "65547dca2fmshd461c5742ef8e50p10016fjsn3e95b74b4b44"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)