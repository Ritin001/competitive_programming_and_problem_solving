n=int(input())
arr=list(map(int,input().split()))
left=0
right=n-1
while(left<=right):
    if (left==right):
        print(arr[left])
    else:
        print(arr[left],arr[right])
    left+=1
    right-=1
    