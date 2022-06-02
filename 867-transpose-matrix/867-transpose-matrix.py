class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_list = []
        for i in range(len(matrix[0])):
            temp_list = []
            for j in range(len(matrix)):
                temp_list.append(matrix[j][i])
            result_list.append(temp_list)
        return result_list