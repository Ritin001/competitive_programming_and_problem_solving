a=list(map(int,input("enter the elements of array").split()))
target=int(input("enter the target element"))
if target in a:
    print(a.index(target))
else:
    for i in range(len(a)-1):
        if a[i]<target and a[i+1]>target:
            print(i+1)
