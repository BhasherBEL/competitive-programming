import random

def hillClimbing(initial, get_neighbors, f):
    current = (f(initial), initial)

    while current:
        nexts = [
            (f(neighbor), neighbor)
            for neighbor in get_neighbors(current[1])
            if f(neighbor) > current[0]
        ]

        if nexts:
            current = random.choice(nexts)
        else:
            return current