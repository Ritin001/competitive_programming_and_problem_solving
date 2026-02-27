a=int(input("enter the no of elements"))
ls = list(map(int,input("ebter the elemets").split()))
min = ls[0]
for i in range(1,len(ls)):
    if ls[i] < min:
        min = ls[i]
print(min) 