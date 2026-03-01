a=3
temp =[1,1]
ps=[[1]]
if a==1:
    print(ps)
elif a>1:
    for i in range(1,a):
        ps.append(temp)
        temp2=[1]
        for j in range(len(temp)-1):
            temp2.append(temp[j]+temp[j+1])
        temp2.append(1)
        temp=temp2
print(ps)