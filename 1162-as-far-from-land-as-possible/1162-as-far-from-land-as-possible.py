class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.cnt = 0
        # URDL directions
        self.directions = [(-1, 0), (0, 1), (1, 0),  (0, -1)]
        q = deque([])
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1 and self.isBorder(r, c, n):
                    q.append((r, c))
        if q:
            self.bfs(q, n)
        else:
            return -1
        return -self.cnt
    
    def isBorder(self, r, c, n):
        for x, y  in self.directions:
            adj_r = r + x
            adj_c = c + y
            if adj_r >= 0 and adj_r < n and adj_c >= 0 and adj_c < n and self.grid[adj_r][adj_c] == 0:
                return True
    def bfs(self, q, n):
        dis = 1
        while q:
            dis -= 1
            self.cnt = min(self.cnt, dis)
            for i in range(len(q)):
                node = q.popleft()
                r, c = node[0], node[1]
                for x, y in self.directions:
                    adj_r = r + x
                    adj_c = c + y
                    if adj_r >= 0 and adj_r < n and adj_c >= 0 and adj_c < n and self.grid[adj_r][adj_c] == 0:
                        self.grid[adj_r][adj_c] = dis - 1
                        q.append((adj_r, adj_c))
        pass