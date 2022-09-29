class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.m = len(maze)
        self.n = len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        self.steps = 0
        self.bfs(maze, entrance)
        return self.steps
        
    def bfs(self, maze: List[List[str]], root: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([root])
        while q:
            self.steps += 1
            for i in range(len(q)):
                node = q.popleft()
                r, c = node[0], node[1]
                # check exit
                
                for direction in directions:
                    nextR = r + direction[0]
                    nextC = c + direction[1]
                    if self.check(nextR, nextC) and maze[nextR][nextC] == ".":
                        if self.isExit(nextR, nextC):
                            # print("find", self.steps)
                            return 1
                        maze[nextR][nextC] = "+"
                        q.append([nextR, nextC])
        self.steps = -1
    
    def check(self, r, c: int) -> bool:
        if r >= 0 and r < self.m and c >= 0 and c < self.n:
            return True
        else:
            return False
    
    def isExit(self, r, c: int) -> bool:
        if r == 0 or c == 0 or r == self.m - 1 or c == self.n - 1:
            return True
        else:
            False