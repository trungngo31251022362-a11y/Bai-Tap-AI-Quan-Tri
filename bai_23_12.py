def nearest_neighbor(start_node, points):
    path = [start_node]
    unvisited = list(points)
    while unvisited:
        last = path[-1]
        next_node = min(unvisited, key=lambda p: distance.euclidean(last, p))
        path.append(next_node)
        unvisited.remove(next_node)
    path.append(start_node) 
    return path
warehouse = (10.776, 106.690)
delivery_points = [(10.78, 106.70), (10.77, 106.71), (10.79, 106.68), (10.76, 106.67)]
optimized_route = nearest_neighbor(warehouse, delivery_points)
m_route = folium.Map(location=warehouse, zoom_start=14)
folium.PolyLine(optimized_route, color='blue', weight=3).add_to(m_route)
m_route.save("23_12_vrp_heuristic.html")
