from bfs.iterative import bfs
from dfs.iterative import dfs
from dls.iterative import dls
from iddfs.iterative import iddfs
from bdbfs.iterative import bdbfs


def get_path(predecessors, goal):
    if not predecessors:
        return

    path = [goal]

    while predecessors[goal]:
        goal = predecessors[goal]
        path.append(goal)

    return path[::-1]


def get_bipath(predecessors, successors, middle):
    if not middle or not predecessors or not successors:
        return

    path = [middle]

    current = middle

    while predecessors[current]:
        current = predecessors[current]
        path.append(current)

    path = path[::-1]

    current = middle

    while successors[current]:
        current = successors[current]
        path.append(current)
    
    return path


def build_predecessors(neighbors):
    predecessors = {x: set() for x in neighbors.keys()}

    for f, ts in neighbors.items():
        for t in ts:
            predecessors[t].add(f)

    return predecessors
def get_path(predecessors, goal):
    if not predecessors:
        return

    path = [goal]

    while predecessors[goal]:
        goal = predecessors[goal]
        path.append(goal)

    return path[::-1]


def get_bipath(predecessors, successors, middle):
    if not middle or not predecessors or not successors:
        return

    path = [middle]

    current = middle

    while predecessors[current]:
        current = predecessors[current]
        path.append(current)

    path = path[::-1]

    current = middle

    while successors[current]:
        current = successors[current]
        path.append(current)
    
    return path


def build_predecessors(neighbors):
    predecessors = {x: set() for x in neighbors.keys()}

    for f, ts in neighbors.items():
        for t in ts:
            predecessors[t].add(f)

    return predecessors