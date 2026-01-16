io,md=input("enter the no of numbers and modulo value").split()
sum=0
print("enter the numbers")
num = list(map(int, input().split()))
for i in num:
    sum = sum + i
modulo = int(sum) % int(md)
print(modulo)    