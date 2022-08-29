class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for i in range(col)] for j in range(row)]
        def bfs(grid, visited, s_node, cnt, row , col):
            q = deque([s_node])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    r = node[0]
                    c = node[1]
                    grid[r][c] = cnt
                    visited[r][c] = 1
                    if r > 0 and grid[r-1][c] != "0" and visited[r-1][c] == 0:
                        visited[r-1][c] = 1
                        q.append((r-1, c))
                    if c > 0 and grid[r][c-1] != "0" and visited[r][c-1] == 0:
                        visited[r][c-1] = 1
                        q.append((r,c-1))
                    if r + 1 < row and grid[r+1][c] != "0" and visited[r+1][c] == 0:
                        visited[r+1][c] = 1
                        q.append((r+1, c))
                    if c + 1 < col and grid[r][c+1] != "0" and visited [r][c+1] == 0:
                        visited[r][c+1] == 1
                        q.append((r, c+1))
                    
        for r in range(row):
            for c in range(col):
                # If this is a unvisited island, bfs the island and color it with cnt
                if visited[r][c] == 0 and grid[r][c] != "0":
                    cnt += 1
                    bfs(grid, visited, (r,c),cnt, row, col)
        return cnt
                    