nums=list(map(int,input("enter the elements of array").split()))
k=int(input("enter the value of k"))
nums.sort()
print(nums[k*-1])
