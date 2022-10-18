class Solution:
    def __init__(self):
        self.record = {0: 0}
        
    def countBits(self, n: int, upper = -1) -> List[int]:
        if n == 0:
            return [0]
        if n in self.record:
            return self.countBits(n-1, upper) + [self.record[n]]
        if upper == -1:
            upper = self.findUpper(n)
        bound = pow(2, upper)
        while bound > n:
            upper -= 1
            bound = pow(2, upper)
        pre = self.countBits(n-1, upper)
        self.record[n] = 1 + self.record[n - bound]
        return pre + [self.record[n]]
            
    def findUpper(self, n: int) -> int:
        cnt = -1
        while n > 0:
            n >>= 1
            cnt += 1
        return cnt