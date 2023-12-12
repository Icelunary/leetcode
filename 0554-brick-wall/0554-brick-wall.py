class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        cross = defaultdict(int)
        cross[0] = 0
        # print(cross)
        for r in wall:
            idx = 0
            for length in r[:-1]:
                idx += length
                cross[idx] += 1
        return n - max(cross.values())
