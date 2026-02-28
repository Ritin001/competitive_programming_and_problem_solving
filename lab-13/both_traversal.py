a=int(input("enter the number of cars"))
ls=list(map(int,input("enter the cars in order").split()))
i,j = 0,a-1
while j>=i:
    if i==j:
        print(ls[i],end=" ")
    else:
        print(ls[i],ls[j],end=" ")
    i+=1
    j-=1
