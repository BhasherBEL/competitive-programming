from collections import deque


def bdbfs(root, goal, get_neighbours, get_predecessor):
    que1 = deque()
    que2 = deque()
    que1.append(root)
    que2.append(goal)
    explored1 = {root: None}
    explored2 = {goal: None}

    while que1 and que2:
        v1 = que1.popleft()
        v2 = que2.popleft()

        if v1 in explored2: 
            return explored1, explored2, v1
        if v2 in explored1:
            return explored1, explored2, v2

        for edge in get_neighbours(v1):
            if edge not in explored1:
                que1.append(edge)
                explored1[edge] = v1

        for edge in get_predecessor(v2):
            if edge not in explored2:
                que2.append(edge)
                explored2[edge] = v2
