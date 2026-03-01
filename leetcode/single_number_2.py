a=list(map(int,input("enter the elements of array").split()))
a2=set(a)
for i in a2:
    if i in a:
        a.remove(i)
for i in a2:
    if i not in a:
        print(i)