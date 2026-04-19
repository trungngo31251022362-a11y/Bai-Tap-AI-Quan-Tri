import folium
dc_coords = (10.7800, 106.6850)
m = folium.Map(location=dc_coords, zoom_start=12)
folium.Marker(dc_coords, popup="Trung tâm phân phối (Kho chính)", icon=folium.Icon(color='black', icon='home')).add_to(m)
radii = {
    "Vùng 1 (3 km)": {"radius": 3000, "color": "green"},
    "Vùng 2 (5 km)": {"radius": 5000, "color": "blue"},
    "Vùng 3 (10 km)": {"radius": 10000, "color": "red"}
}
for name, props in radii.items():
    folium.Circle(
        location=dc_coords,
        radius=props["radius"],
        color=props["color"],
        fill=True,
        fill_opacity=0.1,
        popup=name
    ).add_to(m)
m.save('map_23_5_service_area.html')
print("Đã xuất bản đồ Vùng phục vụ ra file map_23_5_service_area.html")
