class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        dpRow = [0] * len(grid)
        dpCol = [0] * len(grid[0])
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dpRow[r] += 1
                    dpCol[c] += 1
                else:
                    dpRow[r] -= 1
                    dpCol[c] -= 1
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = dpRow[r] + dpCol[c]
        
        return ans