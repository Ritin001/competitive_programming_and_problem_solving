def fact(n,k):
    if n == 1 or n ==0 or n==k:
        return 1
    else:
        return n * fact(n-1,k)
    
def fact_div(n,k):
    return fact(n,max(k,n-k))//fact(min(k,n-k),0)

n,d,k,r =map(int,input("enter the value of n,d,k and r").split())


print("%.4f" %(fact_div(d,r)*fact_div(n-d,k-r)/fact_div(n,k)))
