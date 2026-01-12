n =int(input("given the number of items"))
sum_after_discount = 0
for i in range(n):
    price,discount=input("give the price and discount ").split()
    sum_after_discount=sum_after_discount + (int(price)-(int(price)* int(discount)/100))
discount=max(150,sum_after_discount*0.1)
sum_after_discount = sum_after_discount -discount
print("the final discount is ", sum_after_discount)
