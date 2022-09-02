class Solution:
    status = []
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        m = len(heights)
        n = len(heights[0])
        self.initializeStatus(m, n)
        self.initBorderStatus(m, n)
        # for i in self.status:
        #     print(i)
        # print()
        self.update_status(m ,n)
        # for i in self.status:
        #     print(i)
        res = []
        for r in range(m):
            for c in range(n):
                if self.status[r][c] == (1, 1):
                    res.append([r, c])
        return res
    
    def bfs(self, start, row, col):
        q = deque([start])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                r = node[0]
                c = node[1]
                # For each, check adj, height condition and if status need to be updated
                # Check top
                if r > 0 and self.heights[r-1][c] >= self.heights[r][c] and self.check_status(node, (r-1, c)):
                    q.append((r-1, c))
                # Check left
                if c > 0 and self.heights[r][c-1] >= self.heights[r][c] and self.check_status(node, (r, c-1)):
                    q.append((r,c-1))
                # Check down
                if r + 1 < row and self.heights[r+1][c] >= self.heights[r][c] and self.check_status(node, (r+1, c)):
                    q.append((r+1, c))
                # Check right
                if c + 1 < col and self.heights[r][c+1] >= self.heights[r][c] and self.check_status(node, (r, c+1)):
                    q.append((r, c+1))
                # if node == (1,0):
                #     print("This is q:", q)
                #     print(c + 1 < col)
                #     print(self.heights[r][c+1], self.heights[r][c], r, c)
                #     print(self.check_status(node, (r, c+1)))
    
    def initializeStatus(self, row, col):
        self.status = [[(0, 0) for i in range(col)] for j in range(row)]
    
    def initBorderStatus(self, row, col):
        # init left and right status
        for i in range(row):
            self.status[i][0] = (1, self.status[i][0][1])
            self.status[i][-1] = (self.status[i][-1][0], 1)
        
        # init top and bottom status
        for i in range(col):
            self.status[0][i] = (1, self.status[0][i][1])
            self.status[-1][i] = (self.status[-1][i][0], 1)
    
    def check_status(self, point, adjPoint) -> bool:
        point_r = point[0]
        point_c = point[1]
        adj_r = adjPoint[0]
        adj_c = adjPoint[1]
        res = False
        p, a = self.status[adj_r][adj_c][0], self.status[adj_r][adj_c][1]
        if self.status[point_r][point_c][0] > self.status[adj_r][adj_c][0]:
            p = self.status[point_r][point_c][0]
            res = True
        if self.status[point_r][point_c][1] > self.status[adj_r][adj_c][1]:
            a = self.status[point_r][point_c][1]
            res = True
        self.status[adj_r][adj_c] = (p, a)
        # if res == True:
        #     for i in self.status:
        #         print(i)
        #     print()
        return res
    
    def update_status(self, row, col):
        for i in range(row):
            # print("updated from", (i,0), (i,-1))
            self.bfs((i, 0), row, col)
            self.bfs((i, col - 1), row, col)
        for i in range(col):
            # print("updated from", (0,i),(-1, i))
            self.bfs((0, i), row, col)
            self.bfs((row - 1, i), row, col)