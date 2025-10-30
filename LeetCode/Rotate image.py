# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# n= len(matrix[0])

# for j in range(n):
#     d = matrix[j][n-j-1]
#     for i in range(n-1-j):
#         # print(matrix[j][i],' ' ,matrix[i][n-j-1] )
#         # print(i,j,n-j-1)

        


#         xy  = matrix[i][n-j-1]

#         matrix[i][n-j-1] = matrix[j][i] 
#     matrix[i+1][n-j-1] = d

        


# print(matrix)



"""
1 1      1 4
1 2      2 4
1 3      3 4
1 4      4 4


2 1      1   3
2 2      2   3
2 3      3   3
2 4      4   3

"""



matrix  = [[1,2,3],[4,5,6],[7,8,9]]


n= len(matrix[0])
rotated_matrix = []
for j in range(n):
    row = []
    for i in range(n):
        row.append(matrix[n-1-i][j])
    rotated_matrix.append(row)

matrix = rotated_matrix
  


print(matrix)
