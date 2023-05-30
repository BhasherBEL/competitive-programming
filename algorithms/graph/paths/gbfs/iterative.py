from collections import deque


def gbfs(root, goal, get_neighbours, get_h):
    que = deque([(get_h(root, goal), root)])
    explored = {root: None}

    while que:
        _, v = que.popleft()
        if v == goal:
            return explored

        for edge in get_neighbours(v):
            if edge not in explored:
                que.append((get_h(edge, goal), edge))
                explored[edge] = v

