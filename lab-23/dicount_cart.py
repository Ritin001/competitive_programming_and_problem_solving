n=int(input())
items={}
for i in range(n):
    name,price = input().split()
    items[name]=int(price)
m=int(input())
total=0
for i in range(m):
    name,discount =input().split()
    discount=int(discount)
    items[name]=items[name]*(100-discount)/100
    total+=items[name]

c,t=map(int,input().split())
if total>t:
    total-c
for i in items:
    print(f"{i}: {items[i]:.2f}")
print(f"Total: {total:.2f}")