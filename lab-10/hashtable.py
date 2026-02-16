a=int(input("enter the no of input"))
list_a=[]
for i in range(a):
    aa=input("enter the name")
    list_a.append(aa)
b=int(input("enter the no of input"))
for i in range(b):
    bb=input("enter the name")
    if bb in list_a:
        print("found")
    else:
        print("not found")