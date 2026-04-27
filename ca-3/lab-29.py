import heapq

def fastest_path(graph, start, end, max_time):
    pq = [(0, 0, start)]
    visited = {}

    while pq:
        time, cost, node = heapq.heappop(pq)

        if node == end:
            return time, cost

        if node in visited and visited[node] <= time:
            continue

        visited[node] = time

        for neighbor, t, c in graph[node]:
            new_time = time + t
            new_cost = cost + c

            if new_time <= max_time:
                heapq.heappush(pq, (new_time, new_cost, neighbor))

    return -1


n = int(input("Enter number of nodes: "))
graph = {}

for _ in range(n):
    node = input("Enter node: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v, t, c = input("Enter u v time cost: ").split()
    graph[u].append((v, int(t), int(c)))

start = input("Enter start: ")
end = input("Enter end: ")
max_time = int(input("Enter max time: "))

print("Fastest path:", fastest_path(graph, start, end, max_time))