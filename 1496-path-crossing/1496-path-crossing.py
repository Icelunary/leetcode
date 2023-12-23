class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        visited = set()
        cur = [0, 0]
        visited.add((cur[0], cur[1]))
        for direction in path:
            nexX, nexY = cur[0] + directions[direction][0], cur[1] + directions[direction][1]
            # print(visited)
            # print((nexX, nexY))
            if (nexX, nexY) in visited:
                return True
            cur = [nexX, nexY]
            visited.add((nexX, nexY))
        
        return False