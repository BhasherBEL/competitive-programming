from collections import deque


def bfs(root, goal, get_neighbours):
    que = deque()
    que.append(root)
    explored = {root: None}

    while que:
        v = que.popleft()
        if v == goal:
            return explored

        for edge in get_neighbours(v):
            if edge not in explored:
                que.append(edge)
                explored[edge] = v
