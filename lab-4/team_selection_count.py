def fact(n,k):
    if n == 1 or n ==0 or n==k:
        return 1
    else:
        return n * fact(n-1,k)
n,k =map(int,input("enter the value of n and k").split())
if n<=1000 and n >=k:
    print(fact(n,max(k,n-k))//fact(min(k,n-k),0))
else:
    print("error in the input please check and enter again")