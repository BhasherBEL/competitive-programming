import random

def hillClimbing(initial, get_neighbors, f, p=0.2):
    current = (f(initial), initial)

    while current:
        nexts = [
            (f(neighbor), neighbor)
            for neighbor in get_neighbors(current[1])
            if f(neighbor) > current[0] or random.random() < p
        ]

        if nexts:
            current = random.choice(nexts)
        else:
            return current