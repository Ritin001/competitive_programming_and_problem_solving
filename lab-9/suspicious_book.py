a=int(input("enter the number of elements"))
arr = list(map(int,input("enter the elements").split()))
tar,r = map(int,input("enter the tar and range").split())
if tar in arr[0:r] :
    print("valid access")
elif tar in arr:
    print("invalid access")
else:
    print("not found")