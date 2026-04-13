n,e= map(int,input("enter the edges and nodes").split())
adj_matrix=[[0]*n for _ in range(n)]
adj_list =[[] for _ in range(n)]
for i in range(e):
    u,v=map(int,input().split())

    adj_matrix[u][v]=1
    adj_matrix[u][v]=1

    adj_list[u].append(v)
    adj_list[v].append(u)


b,l=map(int,input().split())
if adj_matrix[b][l]==1:
    print("connection is there")
else:
    print("connection is not there")
    