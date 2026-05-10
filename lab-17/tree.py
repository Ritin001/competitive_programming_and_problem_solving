from collections import deque
def bfs(graph, start):
    visited= set()
    queue= deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for nieghbour in graph[node]:
                if nieghbour not in visited:
                    queue.append(nieghbour)
    print()
def dfs(graph,node,visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start='A'
bfs(graph, start)
visited= set()
dfs(graph,start,visited)