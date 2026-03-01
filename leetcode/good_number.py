def good_number(n):
    a=list(map(int,str(n)))
    for i in range(len(a)):
        if i%2 ==0 and a[i]%2!=0:
            return False
        elif i%2!=0 and a[i] not in [2,3,5,7]:
            return False
    return True
n=int(input("enter the number"))
count=0
if n==1:
    start =0
else: start = 10**(n-1)
for i in range(start, 10**n):
    if good_number(i):
        count+=1
print(count)