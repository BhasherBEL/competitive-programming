import heapq

def dijkstra(root, goal, get_neighbours, get_dist):
    pq = [(0, root)]
    visited = {root: None}

    while pq:
        d, v = heapq.heappop(pq)

        if v == goal:
            return visited

        for n in get_neighbours(v):
            if n not in visited:
                heapq.heappush(pq, (d + get_dist(v, n), n))
                visited[n] = v


