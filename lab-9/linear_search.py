a=int(input("enter the number of elements"))
arr = list(map(int,input("enter the timing").split()))
tar = int(input("target:"))
check=False
for i in range(a):
    if tar == arr[i]:
        print(i)
        check=True
        break
if check==False:
    print("not found")