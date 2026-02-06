n=int(input("enter the no of students"))
a = list(map(int,input("enter the timing").split()))
for i in range(3):
    for j in range(n-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[-3])