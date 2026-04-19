import folium
import pandas as pd
import numpy as np
from scipy.spatial import distance
customers = np.array([[10.772, 106.698], [10.782, 106.685], [10.775, 106.701], [10.785, 106.710], [10.765, 106.690]])
drivers = np.array([[10.770, 106.695], [10.780, 106.705], [10.760, 106.680]])
m = folium.Map(location=[10.775, 106.695], zoom_start=14)
dist_matrix = distance.cdist(customers, drivers)
assignments = np.argmin(dist_matrix, axis=1) 
for i, cust_coord in enumerate(customers):
    driver_idx = assignments[i]
    driver_coord = drivers[driver_idx]
    folium.Marker(cust_coord, popup=f"Khách {i+1}", icon=folium.Icon(color='blue', icon='user')).add_to(m)
    folium.Marker(driver_coord, popup=f"Tài xế {driver_idx+1}", icon=folium.Icon(color='red', icon='car')).add_to(m)
    folium.PolyLine([cust_coord, driver_coord], color='green', weight=2, opacity=0.8, dash_array='10').add_to(m)
m.save("23_8_ride_matching.html")
print("Đã tạo mô phỏng gọi xe công nghệ.")
