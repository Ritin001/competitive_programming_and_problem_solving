n=int(input("enter the size of array"))
a = list(map(int,input("enter the elements of array").split()))
checksum = int(input("enter the checksum"))
ue=0
for i in a:
    ue ^= i

if len(a) != n:
    print("anomaly")
elif ue== checksum:
    print("ok")
else:
    print("anomaly")