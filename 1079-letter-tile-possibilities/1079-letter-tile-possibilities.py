class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.cnt = {}
        self.res = 0
        for tile in tiles:
            if tile in self.cnt:
                self.cnt[tile] += 1
            else:
                self.cnt[tile] = 1
        self.backtrack()
        return self.res
    
    def backtrack(self):
        for k in self.cnt:
            if not self.cnt[k]:
                continue
            else:
                self.cnt[k] -= 1
                self.res += 1
                self.backtrack()
                self.cnt[k] += 1