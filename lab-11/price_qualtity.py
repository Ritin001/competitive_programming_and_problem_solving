n=int(input("enter the input"))
a= list(map(int,input("enter the price").split()))
b= list(map(int,input("enter the quantity").split()))
sum =0
for i in range(n):
    sum= sum +(a[i]*b[i])
print()
print("total price : ",sum)