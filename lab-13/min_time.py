a=int(input("no of cars: "))
ls1=list(map(int,input("enter the cars in order").split()))
ls2=list(map(int,input("enter the speed of cars in order").split()))
max=0
for i in range(a):
    if max<ls1[i]/ls2[2]:
        max=ls1[i]/ls2[2]

print(int(max))