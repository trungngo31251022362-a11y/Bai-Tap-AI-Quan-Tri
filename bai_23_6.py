import osmnx as ox
import networkx as nx
place_name = "District 1, Ho Chi Minh City, Vietnam"
print(f"Đang tải dữ liệu giao thông cho {place_name}...")
G = ox.graph_from_place(place_name, network_type='drive')
fig, ax = ox.plot_graph(G, show=False, close=False, edge_color='gray')
stats = ox.basic_stats(G)
print("\n--- THỐNG KÊ MẠNG LƯỚI GIAO THÔNG ---")
print(f"Số lượng nút giao (Nodes/Intersections): {stats['n']}")
print(f"Số lượng đoạn đường (Edges/Streets): {stats['m']}")
print(f"Chiều dài trung bình một đoạn đường: {stats['edge_length_avg']:.2f} mét")
print(f"Mật độ nút giao (Node density): {stats['node_density_km']:.2f} nút/km2")
