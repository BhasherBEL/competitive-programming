from collections import deque
from dls.iterative import dls

def iddfs(root, goal, get_neighbours, max_depth=10):
    for i in range(max_depth+1):
        if res := dls(root, goal, get_neighbours, max_depth=i):
            return res