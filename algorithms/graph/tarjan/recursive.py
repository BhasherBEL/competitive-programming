def tarjan(root, get_neighbors):
    def dfs(node, parent):
        nonlocal i
        discovery[node] = low[node] = i 
        i += 1

        for neighbor in get_neighbors(node):
            if neighbor == parent:
                continue

            if neighbor not in discovery:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.add((node, neighbor))
            else:
                low[node] = min(low[node], discovery[neighbor])

    i = 0

    discovery = {} 
    low = {} 

    bridges = set()

    dfs(root, None)

    return bridges

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

    print(tarjan('A', lambda x: neighbors[x]))