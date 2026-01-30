def fact(n,k):
    if n == 1 or n ==0 or n==k:
        return 1
    else:
        return n * fact(n-1,k)
    
def fact_div(n,k):
    return fact(n,max(k,n-k))//fact(min(k,n-k),0)

k,r =map(int,input("enter the value of k and r").split())


print("%.6f" %(fact_div(13,r)*fact_div(39,k-r)/fact_div(52,k)))