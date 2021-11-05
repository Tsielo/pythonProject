import requests

url = "https://weatherapi-com.p.rapidapi.com/ip.json"

querystring = {"q":"<REQUIRED>"}

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "65547dca2fmshd461c5742ef8e50p10016fjsn3e95b74b4b44"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)