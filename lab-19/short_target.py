import heapq

n, m = map(int, input("enter n, m: ").split())

graph = {i: [] for i in range(n)}

for _ in range(m):
    u, v, w = map(int, input("enter u, v, w: ").split())
    graph[u].append((v, w))

def dijkstra(start, target):
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)

        # 🔥 Early stop when target is reached
        if node == target:
            return d

        # Skip outdated entries
        if d > dist[node]:
            continue

        for neighbour, weight in graph[node]:
            new_dist = d + weight

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(pq, (new_dist, neighbour))

    return -1   # if target not reachable


start = int(input("enter start node: "))
target = int(input("enter target node: "))

print(dijkstra(start, target))