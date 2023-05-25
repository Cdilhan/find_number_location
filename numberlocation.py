import phonenumbers
from mynumber import number

import folium
from phonenumbers import geocoder


key='8d53ce0209c74e6c9fd3c56bc03c94f0'

chandupanumber=phonenumbers.parse(number)

yourlocation=geocoder.description_for_number(chandupanumber,"en")

print(yourlocation)
from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)

query=str(yourlocation)

result=geocoder.geocode(query)

print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourlocation).add_to((myMap))
myMap.save("mylocation.html")

