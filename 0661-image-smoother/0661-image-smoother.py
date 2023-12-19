class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0],
                      [-1, 1], [0, 1], [1, 1]]
        m = len(img)
        n = len(img[0])
        
        def surround(x: int, y: int) -> int:
            tot = 0
            num = 0
            # print(x, y)
            for x_offset, y_offset in directions:
                new_x = x + x_offset
                new_y = y + y_offset
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    tot += img[new_x][new_y]
                    num += 1
                # print(new_x, new_y, tot, num)
            
                    
            return tot // num
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = surround(r, c)
        return ans