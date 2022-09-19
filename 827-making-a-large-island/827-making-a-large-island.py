class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.grid = grid
        cnt = 2
        res = 1
        myMap = {0: 0}
        for r in range(self.n):
            for c in range(self.n):
                if grid[r][c] == 1:
                    size = self.bfs((r, c), cnt)
                    res = max(size, res)
                    myMap[cnt] = size
                    cnt += 1
        # print(self.grid)
        # print()
        # print(myMap)
        
        for r in range(self.n):
            for c in range(self.n):
                if not self.grid[r][c]:
                    islands = self.getIslands(r, c)
                    # print(r, c, islands)
                    cur = 1
                    for island in islands:
                        cur += myMap[island]
                    res = max(cur, res)
        return res
    
    def bfs(self, loc, cnt):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque([loc])
        self.grid[loc[0]][loc[1]] = cnt
        size = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for direction in directions:
                    nextR = r + direction[0]
                    nextC = c + direction[1]
                    if self.checkBorder(nextR, nextC) and self.grid[nextR][nextC] == 1:
                        self.grid[nextR][nextC] = cnt
                        size += 1
                        q.append((nextR, nextC))
        return size
                
    def checkBorder(self, r, c):
        if r < 0 or c < 0 or r >= self.n or c >= self.n:
            return False
        else:
            return True
    
    def getIslands(self, r, c):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        islands = set()
        for direction in directions:
            nextR = r + direction[0]
            nextC = c + direction[1]
            # if self.checkBorder(nextR, nextC):
            #     print(self.grid[nextR][nextC])
            #     print(not self.grid[nextR][nextC])
            if self.checkBorder(nextR, nextC) and self.grid[nextR][nextC]:
                islands.add(self.grid[nextR][nextC])
        return list(islands)
                