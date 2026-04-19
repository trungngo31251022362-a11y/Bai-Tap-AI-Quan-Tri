from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X = np.random.randn(50, 2) * 0.02 + [10.77, 106.69] 
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
centroids = kmeans.cluster_centers_
m_cluster = folium.Map(location=[10.77, 106.69], zoom_start=13)
colors = ['red', 'blue', 'green']
for i, point in enumerate(X):
    label = kmeans.labels_[i]
    folium.CircleMarker(point, radius=5, color=colors[label], fill=True).add_to(m_cluster)
for i, center in enumerate(centroids):
    folium.Marker(center, popup=f"Trạm/Kho đề xuất {i+1}", icon=folium.Icon(color='black', icon='star')).add_to(m_cluster)
m_cluster.save("23_9_clustering.html")
