import heapq
n, m = map(int, input("enter the value of n , m: ").split())
edges=[]
for i in range(m):
    li=list(map(int,input("enter the u,v,w").split())) 
    edges.append(li)
graph = {i :[]for i in range(n)}
for u,v,w in edges:
    graph[u].append((v,w))
def djkstra(start):
    dist=[float('inf')]*n
    dist[start]=0
    pq = [(0,start)]
    while pq :
        d,node =heapq.heappop(pq)
        for neighbour ,weight in graph[node]:
            new_dist =d+weight
            if new_dist<dist[neighbour]:
                dist[neighbour]=new_dist
                heapq.heappush(pq,(new_dist,neighbour))
                return dist
    return dist
print(djkstra(0))
