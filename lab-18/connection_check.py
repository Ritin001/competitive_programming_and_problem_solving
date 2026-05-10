from collections import deque

n,e= map(int,input("enter the edges and nodes").split())
adj_list =[[] for _ in range(n)]
for i in range(e):
    u,v=map(int,input().split())

    adj_list[u].append(v)
    adj_list[v].append(u)

s, d = map(int, input().split()) 
visited = [False] * n
queue=deque([s])
visited[s]=True
found=False
while queue:
    node=queue.popleft()
    if node==d:
        found = True
        break
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            visited[neighbour]=True
            queue.append(neighbour)

if found:
    print("Path exists between the given nodes.")
else:
    print("No path exists between the given nodes.")