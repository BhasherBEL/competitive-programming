import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/paths")

from dls.iterative import dls

def local_bridges(nodes, get_neighbors, depth=2):

    bridges = set()

    for node in nodes:
        for neighbor in get_neighbors(node):
            get_local_neighbors = lambda x: set(get_neighbors(x)) - ({node, neighbor} if x in [node, neighbors] else set())
            if not dls(node, neighbor, get_local_neighbors, max_depth=depth):
                bridges.add(frozenset((node, neighbor)))
    
    return {tuple(bridge) for bridge in bridges}


if __name__ == '__main__':
    neighbors = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G', 'H'],
        'C': ['A', 'D', 'E'],
        'D': ['C', 'E', 'A'],
        'E': ['A', 'C', 'D', 'F'],
        'F': ['B', 'G', 'H', 'E'],
        'G': ['B', 'F', 'H'],
        'H': ['B', 'F', 'G']
    }

    print(local_bridges(neighbors.keys(), lambda x: neighbors[x]))