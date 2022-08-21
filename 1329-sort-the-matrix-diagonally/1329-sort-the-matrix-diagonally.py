class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        print("mat: ", mat)
        matrix = []
        row = len(mat)
        column = len(mat[0])
        for i in range((len(mat) + len(mat[0]) - 1)):
            matrix.append([])
        # print(matrix)
        
        res = [[0 for j in range(column)] for i in range(row)]
        print(res)
        # convert
        for i in range(row):
            for j in range(column):
                matrix[j-i].append(mat[i][j])
        # print("reformed matrix: ", matrix)
        
        # sort
        for lis in matrix:
            lis.sort()
        # print("sorted matrix:", matrix)
        
        for i in range(column):
            vertical = i
            horizontal = 0
            for j in range(len(matrix[i])):
                res[horizontal + j][vertical + j] = matrix[i][j]
        # print(res)
        vertical_part = matrix[column:]
        vertical_part.reverse()
        # print(vertical_part)
        for i in range(1, row):
            vertical = 0
            horizontal = i
            for j in range(len(vertical_part[i-1])):
                res[horizontal + j][vertical + j] = vertical_part[i-1][j]
            
#         print(res)
        return res
        