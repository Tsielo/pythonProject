import http.client 

conn =http.client.HTTPSConnection("http://api.openweathermap.org")

city_name = "Durban"
Lat = "27.8579"
lon = "31.09292"
api_key = "3909b8eec89b6cae621162d45f8b0283"

conn.request("GET", "/data/2.5/weather?q= "lat"+"LON"+ city_name+"&appid="+api_key)

#response = requests.get (url).json ()
res = conn.getresponse()
data = res.read()
print = (data.decode("utf-8"))

