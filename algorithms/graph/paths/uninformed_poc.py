from bfs.iterative import bfs
from dfs.iterative import dfs
from dls.iterative import dls
from iddfs.iterative import iddfs
from bdbfs.iterative import bdbfs
from utils import *


if __name__ == '__main__':
    neighbors = {
        'a': {'b','d'},
        'b': {'c', 'f'},
        'c': {'e', 'g', 'h'},
        'd': {'f'},
        'e': {'b', 'f'},
        'f': {'a', 'i'},
        'g': {'e', 'h'},
        'h': {'a'},
        'i': {'h'},
    }

    predecessors = build_predecessors(neighbors)

    print('BFS', get_path(bfs('a', 'h', lambda x: neighbors[x]), 'h'))
    print('DFS', get_path(dfs('a', 'h', lambda x: neighbors[x]), 'h'))
    print('DLS(m=5)', get_path(dls('a', 'h', lambda x: neighbors[x], 5), 'h'))
    print('IDDFS(m=10)', get_path(iddfs('a', 'h', lambda x: neighbors[x], 10), 'h'))
    print('BDBFS', get_bipath(*bdbfs('a', 'h', lambda x: neighbors[x], lambda x: predecessors[x])))