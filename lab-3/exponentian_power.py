#a b p k 
#if a * b %p is divisble by k print divisible otherwise not divisible
a,b,p,k = map(int,input("give the input of a b p k ").split())
mod_val=(a*b)% p
if mod_val % k == 0:
    print("divisible")
else:
    print("not divisible")
