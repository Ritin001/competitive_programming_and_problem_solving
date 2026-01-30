def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

n,k=map(int,input().split())
print(fact(n)/(fact(k)*fact(n-k)))    

