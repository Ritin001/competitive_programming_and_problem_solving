a =int(input())
arr=[]
dict={}
for i in range(a):
    name , number=input("name and the number").split()
    dict[name]=number
b=int(input("enter the search elements"))
for i in range(b):
    bb=input("enter the name of book")
    if bb in dict:
        print(dict[bb])
    else:
        print("book not found")

