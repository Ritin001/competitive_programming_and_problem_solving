n=int(input("enter the input"))
a= list(map(int,input("enter the numbers").split()))
for i in a:
    print(i,end=" ")
print()
print("total price : ",sum(a))