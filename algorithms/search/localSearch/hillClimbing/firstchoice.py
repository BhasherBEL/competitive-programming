def hillClimbing(initial, get_neighbors, f):
    current = (f(initial), initial)

    while current:
        for neighbor in get_neighbors(current[1]):
            if f(neighbor) > current[0]:
                current = (f(neighbor), neighbor)
                break
        else:
            return current