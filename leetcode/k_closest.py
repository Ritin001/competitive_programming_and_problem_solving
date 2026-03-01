def distance(x,y):
    return(x**2+y**2)**0.5
dis ={}
points = [[1,3],[-2,2]]
k=1
for i in points:
    dis[tuple(i)]=distance(i[0],i[1])
    
for i in range(k):
    max=0
    for j in dis:
        if dis[j]>max:
            max=dis[j]
            element=j
    print(element,end=" ")
    dis[element]=-1