import folium


from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder("<Insert Google Maps API Key Here>")

symbols = {
    "fire":["fire","red"],
    "medical":["plus-sign","lightblue"],
    "food" :['cutlery', "green"] ,
    "shelter" : ['home', 'beige']
}

#this will be replaced with the data coming from nlp database
data = {
    '1727 E 107th St, Los Angeles, CA':"fire",
    '9500 Gilman Dr, La Jolla, CA 92093': "medical",
    '12174 Carmel Mountain Rd, San Diego, CA 92128': 'shelter',
    '880 Summit Blvd, Big Bear Lake, CA 92315' : 'food',
}


#creating a map with default view in United States
m = folium.Map(location=[39.00, -98.21], zoom_start=5)


#creating markers based on data from NLP database
for key, value in data.items():
    emergency = geocoder.get(key)
    lat = emergency[0].geometry.location.lat
    lng = emergency[0].geometry.location.lng
    folium.Marker(
    [lat, lng],
    icon = folium.Icon(color=symbols.get(value)[1],  icon=symbols.get(value)[0])
).add_to(m)
    m.save("m.html")



