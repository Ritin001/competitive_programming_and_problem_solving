n,e= map(int,input("enter the edges and nodes").split())
adj_matrix=[[0]*n for _ in range(n)]
adj_list =[[] for _ in range(n)]
for i in range(e):
    u,v=map(int,input().split())

    adj_matrix[u][v]=1
    adj_matrix[u][v]=1

    adj_list[u].append(v)
    adj_list[v].append(u)

for i in adj_matrix:
    print(i)   
for i in adj_list:
    print(i)

    