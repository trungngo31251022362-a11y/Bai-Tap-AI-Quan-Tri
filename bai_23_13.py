import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
st.set_page_config(layout="wide")
st.title("🚚 Logistics & AI Strategy Dashboard - UEH")
st.sidebar.header("Cấu hình lớp dữ liệu")
show_customers = st.sidebar.checkbox("Hiển thị khách hàng", value=True)
show_service_area = st.sidebar.checkbox("Hiển thị vùng phục vụ (Buffer)", value=True)
buffer_dist = st.sidebar.slider("Bán kính phục vụ (m)", 1000, 5000, 3000)
m = folium.Map(location=[10.776, 106.690], zoom_start=13)
warehouse = [10.776, 106.690]
customers = [[10.780, 106.700], [10.770, 106.685], [10.790, 106.695]]
if show_service_area:
    folium.Circle(warehouse, radius=buffer_dist, color='red', fill=True, opacity=0.2).add_to(m)
folium.Marker(warehouse, popup="Tổng kho", icon=folium.Icon(color='red', icon='home')).add_to(m)
if show_customers:
    for c in customers:
        folium.Marker(c, icon=folium.Icon(color='blue', icon='info-sign')).add_to(m)
col1, col2 = st.columns([3, 1])
with col1:
    st_folium(m, width=800, height=500)
with col2:
    st.write("### Chỉ số vận hành")
    st.metric("Tổng đơn hàng", "150", "+12%")
    st.metric("Shipper đang online", "25", "-2")
    st.write("Bảng dữ liệu khách hàng:")
    st.dataframe(pd.DataFrame(customers, columns=['Lat', 'Lon']))
