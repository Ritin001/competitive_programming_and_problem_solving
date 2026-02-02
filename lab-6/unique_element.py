n=int(input("enter the size of array"))
a = list(map(int,input("enter the elements of array")))
ue=0
for i in a:
    ue ^= i
print("The unique element in the list is:",ue)