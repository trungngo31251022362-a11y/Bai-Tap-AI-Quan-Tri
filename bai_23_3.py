import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random
ueh_coords = (10.7764, 106.6907)
m = folium.Map(location=ueh_coords, zoom_start=14)
heatmap_data = []
for _ in range(100):
    lat = ueh_coords[0] + random.uniform(-0.015, 0.015)
    lon = ueh_coords[1] + random.uniform(-0.015, 0.015)
    heatmap_data.append([lat, lon])
HeatMap(heatmap_data, radius=15, blur=10).add_to(m)
m.save("map_23_1_to_3.html")
print("\nĐã lưu bản đồ thành công vào file 'map_23_1_to_3.html'. Mở file này trên trình duyệt để xem.")
