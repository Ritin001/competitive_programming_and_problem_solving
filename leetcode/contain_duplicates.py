a=list(map(int,input("enter the elements of array").split()))
k=int(input("enter the value of k"))
b=False
for i in range(len(a)-k):
    if a[i]==a[i+k]:
        b=True
    
print(b)