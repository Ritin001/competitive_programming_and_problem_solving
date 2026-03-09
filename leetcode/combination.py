from itertools import combinations
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
print(list(combinations(range(1,n+1),k)))