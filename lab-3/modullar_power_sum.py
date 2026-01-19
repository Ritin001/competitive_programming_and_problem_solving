num,modulo=map(int,input("enter the number,power,modulo").split())
sum=0
for i in range(num):
    a,b=map(int,input("enter the numbers and the power").split())
    sum =sum + a**b
print(sum % modulo)