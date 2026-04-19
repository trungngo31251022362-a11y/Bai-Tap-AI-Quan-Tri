import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random

# Khởi tạo bản đồ với vị trí trung tâm là UEH (59C Nguyễn Đình Chiểu)
ueh_coords = (10.7764, 106.6907)
m = folium.Map(location=ueh_coords, zoom_start=14)

# ==========================================
# BÀI 23.1: Thêm Marker trung tâm và các điểm lân cận
# ==========================================
folium.Marker(
    location=ueh_coords, 
    popup="<b>UEH (Cơ sở A)</b><br>59C Nguyễn Đình Chiểu", 
    tooltip="Trường Đại học",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

# Giả lập 5 địa điểm lân cận (Bệnh viện, TTTM, v.v.)
nearby_places = [
    {"name": "Bệnh viện Từ Dũ", "coords": (10.7681, 106.6853)},
    {"name": "Dinh Độc Lập", "coords": (10.7771, 106.6953)},
    {"name": "Chợ Bến Thành", "coords": (10.7725, 106.6980)},
    {"name": "Saigon Centre (Takashimaya)", "coords": (10.7733, 106.7011)},
    {"name": "Nhà thờ Đức Bà", "coords": (10.7798, 106.6990)}
]

for place in nearby_places:
    folium.Marker(
        location=place["coords"],
        popup=place["name"],
        icon=folium.Icon(color='blue')
    ).add_to(m)
