from collections import deque

def bfs(root, goal, get_neighbours):
    que = deque()
    que.append([root])
    explored = {root}

    while que:
        v = que.popleft()
        if v[-1] == goal:
            return v

        for edge in get_neighbours(v[-1]):
            if edge not in explored:
                que.append(v + [edge])
                explored.add(edge)