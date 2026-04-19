import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random
ueh_coords = (10.7764, 106.6907)
m = folium.Map(location=ueh_coords, zoom_start=14)
geolocator = Nominatim(user_agent="logistics_routing_app")
print("--- Khoảng cách từ UEH đến các điểm lân cận ---")
for place in nearby_places:
    dist = geodesic(ueh_coords, place["coords"]).kilometers
    print(f"- {place['name']}: {dist:.2f} km")
    folium.PolyLine(
        locations=[ueh_coords, place["coords"]],
        color='gray',
        weight=2,
        dash_array='5, 5'
    ).add_to(m)
