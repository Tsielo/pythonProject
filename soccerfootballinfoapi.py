import requests

url = "https://soccer-football-info.p.rapidapi.com/matches/view/basic/"

querystring = {"i":"1","l":"en_US"}

headers = {
    'x-rapidapi-host': "soccer-football-info.p.rapidapi.com",
    'x-rapidapi-key': "65547dca2fmshd461c5742ef8e50p10016fjsn3e95b74b4b44"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)