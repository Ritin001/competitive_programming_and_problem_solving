def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

a =int(input())
arr=[]
dict={}
for i in range(a):
    sp , tag=map(int,input("enter the timing").split())
    dict[sp]=tag
    arr.append(sp)

sorted_a = merge_sort(arr)
for i in range (-1,-11,-1):
    tag_no=dict.get(sorted_a[i])
    print(tag_no)
