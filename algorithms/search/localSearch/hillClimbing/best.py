def hillClimbing(initial, get_neighbors, f):
    current = (f(initial), initial)

    while current:
        lc = current
        for neighbor in get_neighbors(current[1]):
            if f(neighbor) > current[0]:
                current = (f(neighbor), neighbor)

        if lc == current:
            return current