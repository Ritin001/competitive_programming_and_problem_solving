n, e = map(int, input().split())

edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

start = int(input())

graph = build_graph(edges, n)

print("BFS:", bfs(graph, start))
print("DFS:", dfs(graph, start))