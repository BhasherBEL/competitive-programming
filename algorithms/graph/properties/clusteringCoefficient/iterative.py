def clustering_coefficient(root, get_neighbors):
    root_neighbors = set(get_neighbors(root))

    friend_pairs = 0

    for neighbor in root_neighbors:
        friend_pairs += len(root_neighbors.intersection(get_neighbors(neighbor)))

    return friend_pairs / 2 / len(root_neighbors)


if __name__ == '__main__':
    neighbors = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G', 'H'],
        'C': ['A', 'D', 'E'],
        'D': ['C', 'E', 'A'],
        'E': ['A', 'C', 'D'],
        'F': ['B', 'G', 'H'],
        'G': ['B', 'F', 'H'],
        'H': ['B', 'F', 'G']
    }

    print(clustering_coefficient('C', lambda x: neighbors[x]))