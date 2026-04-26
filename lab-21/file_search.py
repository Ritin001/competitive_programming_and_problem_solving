from collections import defaultdict 
n = int(input()) 
tree = defaultdict(list) 
file_index = {} 
for _ in range(n): 
    directory, file = input().split() 
    tree[directory].append(file) 
    file_index[file] = directory 
target_file = input() 
for directory in tree:
    print(directory,"->",*tree[directory])
if target_file in file_index:
    print("File found in directory:", file_index[target_file])
else:
    print("File not found")
