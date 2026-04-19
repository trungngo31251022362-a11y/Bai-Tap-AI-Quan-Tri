import osmnx as ox
G = ox.graph_from_place("District 1, Ho Chi Minh City, Vietnam", network_type='drive')
node_degrees = dict(G.degree())
nc = ox.plot.get_node_colors_by_attr(G, "street_count", cmap="YlOrRd") 
fig, ax = ox.plot_graph(G, node_color=nc, node_size=30, edge_linewidth=0.5)
