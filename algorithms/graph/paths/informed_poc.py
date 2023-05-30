import osmnx as ox
import webbrowser
import time

from utils import *
from dijkstra.iterative import dijkstra
from astar.iterative import astar
from smastar.iterative import smastar


if __name__ == '__main__':
    D = ox.graph_from_point((50.66992, 4.61528), dist=1000, network_type="bike", simplify=True)
    G = ox.utils_graph.get_digraph(D)

    ox.graph_from_xml

    def get_h_dist(x, y):
        X = G.nodes[x]
        Y = G.nodes[y]
        return ((X['x']-Y['x'])**2 + (X['y']-Y['y'])**2)**0.5

    initial = ox.nearest_nodes(G, 4.60509, 50.66981)
    target = ox.nearest_nodes(G, 4.62313, 50.66822)

    st = time.time()
    dijkstra_path = get_path(dijkstra(initial, target, lambda x: G.adj[x].keys(), lambda x, y: G.edges[x, y]['length']), target)
    print(f'dijkstra {(time.time()-st)*1000:.2f}ms')
    st = time.time()
    astar_path = get_path(astar(initial, target, lambda x: G.adj[x].keys(), lambda x, y: G.edges[x, y]['length'], get_h_dist), target)
    print(f'a* {(time.time()-st)*1000:.2f}ms')
    st = time.time()
    smastar_path = get_path(smastar(initial, target, lambda x: G.adj[x].keys(), lambda x, y: G.edges[x, y]['length'], get_h_dist, max_size=10), target)
    print(f'sma* {(time.time()-st)*1000:.2f}ms')

    map = ox.plot_route_folium(D, dijkstra_path, route_color='#00ff00', opacity=0.5)
    map = ox.plot_route_folium(D, astar_path, color='#0000ff', opacity=0.5)
    map = ox.plot_route_folium(D, smastar_path, route_map=map, color='#ff0000', opacity=0.5)
    map.save("/tmp/map.html")
    webbrowser.open("/tmp/map.html")