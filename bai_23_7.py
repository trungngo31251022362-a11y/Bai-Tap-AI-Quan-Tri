import osmnx as ox
import networkx as nx
origin_point = (10.7771, 106.6953)
destination_point = (10.7725, 106.6980)
orig_node = ox.distance.nearest_nodes(G, origin_point[1], origin_point[0])
dest_node = ox.distance.nearest_nodes(G, destination_point[1], destination_point[0])
route_dijkstra = nx.shortest_path(G, orig_node, dest_node, weight='length')
length_dijkstra = nx.shortest_path_length(G, orig_node, dest_node, weight='length')
def heuristic(u, v):
    return ox.distance.great_circle(G.nodes[u]['y'], G.nodes[u]['x'], G.nodes[v]['y'], G.nodes[v]['x'])
route_astar = nx.astar_path(G, orig_node, dest_node, heuristic=heuristic, weight='length')
length_astar = nx.astar_path_length(G, orig_node, dest_node, heuristic=heuristic, weight='length')
print(f"Khoảng cách đi bằng Dijkstra: {length_dijkstra:.2f} mét")
print(f"Khoảng cách đi bằng A*: {length_astar:.2f} mét")
fig, ax = ox.plot_graph_routes(G, routes=[route_dijkstra, route_astar], route_colors=['red', 'blue'], route_linewidths=[4, 2])
