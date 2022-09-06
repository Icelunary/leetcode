class Solution:
    def appealSum(self, s: str) -> int:
        self.cnt = {}
        self.res = 0
        self.dif = 0
        n = len(s)
        comb, pre, res = self.backtrack1(s, 0, n)
        return res
        
    def backtrack(self, s, index, n):
        if index == n:
            return
        # Update cnt
        c = s[index]
        if c in self.cnt:
            if self.cnt[c] == 0:
                self.dif += 1
            self.cnt[c] += 1
        else:
            self.cnt[c] = 1
            self.dif += 1
        
        # emunerate next possibility
        self.backtrack(s, index + 1, n)
        
        # update res
        self.res += self.dif
        
        # delete this char
        self.cnt[c] -= 1
        if self.cnt[c] == 0:
            self.dif -= 1
            
    def backtrack1(self, s, index, n): # return number of comb and total dif starting in index
        if index == n - 1:
            self.updateCnt(s[index], n - index, 1)
            return 1, 1, 1
        comb, pre, total = self.backtrack1(s, index + 1, n)
        sub = 0
        c = s[index]
        if c in self.cnt:
            sub = self.cnt[c]
        currentSum = pre + comb - sub + 1
        total += currentSum
        comb += 1
        self.updateCnt(c, comb, total)
        return comb, currentSum, total
                             
        
    def updateCnt(self, c, comb, total):
        self.cnt[c] = comb
