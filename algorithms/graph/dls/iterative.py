from collections import deque


def dls(root, goal, get_neighbours, max_depth=10):
    que = deque()
    que.append(root)
    explored = {root: None}
    depth = {root: 0}

    while que:
        v = que.pop()
        if v == goal:
            return explored

        if depth[v] >= max_depth:
            continue

        for edge in get_neighbours(v):
            if edge not in explored:
                que.append(edge)
                explored[edge] = v
                depth[edge] = depth[v]+1

