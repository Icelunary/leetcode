class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Get everything that need to be rotated in the first quadrant
        row, col = self.get_rotate_area(n)
        # print(row, col)
        # print(self.get_post_rotate_cells(0, 0, 3))
        for r in range(row + 1):
            for c in range(col + 1):
                # for each cell, get the 4 cells after rotate
                # Then place them back to the matrix
                rotate_list = self.get_post_rotate_cells(r, c, n)
                value = []
                # Get the 4 cells' values
                for cell in rotate_list:
                    temp_r = cell[0]
                    temp_c = cell[1]
                    value.append(matrix[temp_r][temp_c])
                print(rotate_list)
                print(value)
                # matrix[rotate_list[0][0]][rotate_list[0][1]] = value[-1]
                # Rotate their values
                for i in range(0, len(rotate_list)):
                    temp_r = rotate_list[i][0]
                    temp_c = rotate_list[i][1]
                    matrix[temp_r][temp_c] = value[i-1]
    
    def get_post_rotate_cells(self, r: int, c: int, n: int) -> list:
        x = 0
        y = 0
        mid = (n - 1) / 2
        cells = [(r,c)]
        r_dif = mid - r
        c_dif = mid - c
        # print(mid, r_dif, c_dif)
        cells.append((int(mid - c_dif), int(mid + r_dif)))
        cells.append((int(mid + r_dif), int(mid + c_dif)))
        cells.append((int(mid + c_dif), int(mid - r_dif)))
        
        return cells

    
    # def get_first_quadrant(self, r, c, n) -> int, int:
    #     mid = n / 2
    #     r_dif = r - n
    #     c_dif = c - n
    #     if r - n < 0 and c - n < 0:
    #         return 
    
    def get_rotate_area(self, n):
        if n % 2 == 1:
            return n // 2 - 1, n // 2
        else:
            return n // 2 - 1, n // 2 -1
        