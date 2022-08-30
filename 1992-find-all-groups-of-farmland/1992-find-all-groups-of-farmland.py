class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(land)
        col = len(land[0])
        
        def searchForLowerBound(land, r, c, row, col):
            # print("start at: ", r, c)
            x = -1
            y = -1
            for i in range(r, row):
                if land[i][c] != 1:
                    x =  i - r - 1
                    break
            for i in range(c, col):
                if land[r][i] != 1:
                    y = i - c - 1
                    break
            if x == -1:
                x = row - r - 1
            if y == -1:
                y = col - c - 1
            return x, y
            
        for r in range(row):
            for c in range(col):
                if land[r][c] == 1:
                    farm = [r,c]
                    x, y =  searchForLowerBound(land, r, c, row, col)
                    farm.append(r + x)
                    farm.append(c + y)
                    res.append(farm)
                    self.recolore(land, r, c, x, y)
        return res
        
    
    def recolore(self, land, row, col, x, y) -> None:
        for i in range(x + 1):
            for j in range(y + 1):
                # print(row, col, length, i, j)
                land[row + i][col + j] = 0
        # print("recolor:")
        # print(land)