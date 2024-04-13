import requests
import folium

res = requests.get('https://ipinfo.io/')
data = res.json()
#print(data)
location = data['loc'].split(',')
lat = float(location[0])
log = float(location[1])

fg = folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data = (open(r"C:\Users\james\Downloads\US_states.json",'r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup="This is my location",icon=folium.Icon(color="green")))

m = folium.Map(location=[lat,log],zoom_start=7)

m.add_child(fg)
m.save('my_map.html')