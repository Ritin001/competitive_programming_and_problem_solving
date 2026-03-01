def matrix(matrix,index):
    a=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            a.append(matrix[i][j])
    a.sort()
    return a[index-1]
mat=[[1,5,9],[10,11,13],[12,13,15]]
k=8
print(matrix(mat,k))
