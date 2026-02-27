a=int(input("enter the no of cars"))
ls = list(map(int,input("enter the speed").split()))
dist = int(input("enter the distance"))
min = ls[0]
for i in range(1,len(ls)):
    if ls[i] < min:
        min = ls[i]
print(min) 
print(dist/min," hrs")