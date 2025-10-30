class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix[0])
        rotated_matrix = []
        for j in range(n):
            row = []
            for i in range(n):
                row.append(matrix[n-1-i][j])
            rotated_matrix.append(row)
        for j in range(n):
            for i in range(n):
                matrix[j][i] = rotated_matrix[j][i]

  
