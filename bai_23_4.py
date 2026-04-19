import geopandas as gpd
import pandas as pd
import folium
import numpy as np
gdf = gpd.read_file('hcm_districts.geojson') 
districts = gdf['district_name'].unique()
mock_data = pd.DataFrame({
    'district_name': districts,
    'order_volume': np.random.randint(500, 5000, size=len(districts)) 
})
gdf_merged = gdf.merge(mock_data, on='district_name')
m = folium.Map(location=[10.7764, 106.6907], zoom_start=11)
folium.Choropleth(
    geo_data=gdf_merged,
    name='choropleth',
    data=gdf_merged,
    columns=['district_name', 'order_volume'],
    key_on='feature.properties.district_name',
    fill_color='YlOrRd', 
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Số lượng đơn hàng (Volume)'
).add_to(m)
m.save('map_23_4_choropleth.html')
print("Đã xuất bản đồ Choropleth ra file map_23_4_choropleth.html")
