class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt = 0
        row = len(grid1)
        col = len(grid1[0])
        def bfs(grid1, grid, s_node, row , col):
            q = deque([s_node])
            res = True
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    r = node[0]
                    c = node[1]
                    if grid1[r][c] == 0:
                        res = False
                    if r > 0 and grid[r-1][c] == 1:
                        grid[r-1][c] = 0
                        q.append((r-1, c))
                    if c > 0 and grid[r][c-1] == 1:
                        grid[r][c-1] = 0
                        q.append((r,c-1))
                    if r + 1 < row and grid[r+1][c] == 1:
                        grid[r+1][c] = 0
                        q.append((r+1, c))
                    if c + 1 < col and grid[r][c+1] == 1:
                        grid[r][c+1] = 0
                        q.append((r, c+1))
            return res
                    
        for r in range(row):
            for c in range(col):
                # If this is a unvisited island, bfs the island and check if it's sub
                if grid2[r][c] == 1:
                    grid2[r][c] = 0
                    if bfs(grid1, grid2, (r,c), row, col):
                        cnt += 1
        return cnt  
        
        