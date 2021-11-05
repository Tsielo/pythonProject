import requests

url = "https://instagram47.p.rapidapi.com/public_post_comments"

querystring = {"shortcode":"CU4lZWkojkY"}

headers = {
    'x-rapidapi-host': "instagram47.p.rapidapi.com",
    'x-rapidapi-key': "65547dca2fmshd461c5742ef8e50p10016fjsn3e95b74b4b44"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)