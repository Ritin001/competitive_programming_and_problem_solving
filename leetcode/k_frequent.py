a=list(map(int,input("enter the elements of array").split()))
k=int(input("enter the value of k"))
dict={}
a2=set(a)
for i in a2:
    count=0
    for j in a:
        if i==j:
            count+=1
    dict[i]=count
for i in range(k):
    max=0
    for j in dict:
        if dict[j]>max:
            max=dict[j]
            element=j
    print(element,end=" ")
    dict[element]=-1