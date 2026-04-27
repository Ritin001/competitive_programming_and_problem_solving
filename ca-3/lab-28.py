import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if node == end:
            return cost

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return -1


n = int(input("Enter number of nodes: "))
graph = {}

for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v, w = input("Enter u v weight: ").split()
    graph[u].append((v, int(w)))

start = input("Enter start node: ")
end = input("Enter end node: ")

print("Cheapest path cost:", dijkstra(graph, start, end))