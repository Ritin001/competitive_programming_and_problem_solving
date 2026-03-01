a=list(map(int,input("enter the elements of array").split()))
target=int(input("enter the target element"))
if target in a:
    for i in range(len(a)-1):
        if a[i]!=target and a[i+1]==target:
            print(i+1,end=" ")
        elif a[i]==target and a[i+1]!=target:
            print(i)
else:
    print([-1,-1],end=" ")