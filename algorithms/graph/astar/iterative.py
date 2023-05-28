import heapq

def astar(root, goal, get_neighbours, get_dist, get_h):
    pq = [(get_h(root, goal), 0, root)]
    visited = {root: None}

    while pq:
        _, d, v = heapq.heappop(pq)

        if v == goal:
            return visited

        for n in get_neighbours(v):
            if n not in visited:
                nd = d + get_dist(v, n)
                heapq.heappush(pq, (nd + get_h(n, goal), nd, n))
                visited[n] = v


