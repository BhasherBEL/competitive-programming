from collections import deque


def gbst(root, goal, get_neighbours, get_h):
    path = [root]
    explored = {root: None}
    dead = set()

    while path[-1]:
        if path[-1] == goal:
            return explored

        try:
            path.append(
                min(
                    (get_h(edge, goal), edge)
                    for edge
                    in get_neighbours(path[-1])
                    if edge not in explored
                )[1]
            )
        except ValueError:
            path.pop()
        else:
            explored[path[-1]] = path[-2]
