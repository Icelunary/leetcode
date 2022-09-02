class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.res = 0
        for i in grid:
            print(i)
        rowNum = len(grid)
        colNum = len(grid[0])
        for r in range(rowNum):
            for c in range(colNum):
                if grid[r][c] == 1:
                    self.grid[r][c] = 0
                    self.bfs((r,c), rowNum, colNum)
        return self.res
        
    def bfs(self, start, rowNum, colNum):
        q = deque([start])
        area = 0
        while q:
            node = q.popleft()
            r, c = node[0], node[1]
            area += 1
            if r - 1 >= 0 and self.grid[r-1][c] == 1:
                q.append((r-1, c))
                self.grid[r-1][c] = 0
            if c - 1 >= 0 and self.grid[r][c-1] == 1:
                q.append((r, c-1))
                self.grid[r][c-1] =  0
            if r + 1 < rowNum and self.grid[r+1][c] == 1:
                q.append((r+1, c))
                self.grid[r+1][c] = 0
            if c + 1 < colNum and self.grid[r][c+1] == 1:
                q.append((r, c+1))
                self.grid[r][c+1] = 0
        # for i in self.grid:
        #     print(i)
        if area > self.res:
            self.res = area