at= int(input("enter the total purchase amount  "))
if(at>=10000):
    at=at-(at*0.25)-500
elif(at>=5000):
    at=at-(at*0.2)
elif(at>=1000):
    at=at-(at*0.1)
print("the final amount is",int(at))