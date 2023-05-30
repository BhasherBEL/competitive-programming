import heapq

def smastar(root, goal, get_neighbours, get_dist, get_h, max_size=100):
    pq = [(0, get_h(root, goal), root)]
    visited = {root: None}

    while pq:
        _, d, v = heapq.heappop(pq)

        if v == goal:
            return visited

        for n in get_neighbours(v):
            if n not in visited:
                d = d + get_dist(v, n)
                heapq.heappush(pq, (d + get_h(n, goal), d, n))
                visited[n] = v

        if len(pq) > max_size:
            pq.sort()
            pq = pq[:max_size]
            heapq.heapify(pq)


