class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_list = []
        len1 = len(matrix[0])
        len2 = len(matrix)
        for i in range(len1):
            temp_list = []
            for j in range(len2):
                temp_list.append(matrix[j][i])
            result_list.append(temp_list)
        return result_list