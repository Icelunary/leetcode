import math

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        p1 = 0
        p2 = 0
        reachEnd = 0
        result = []
        if s[p2] is not c:
            p2 = self.foundNext(p2, s, c)
        for i in range(len(s)):
            if i > p2 and reachEnd == 0:
                p1 = p2
                p2 = self.foundNext(p2, s, c)
                if p1 == p2:
                    reachEnd = 1
            dis = self.countDistance(p1, i, p2, s, c)
            result.append(dis)
        return result
        
    
    def foundNext(self, p, s, c):
        if p == len(s):
            return p
        for i in range(p + 1, len(s)):
            if s[i] == c:
                return i
        return p
    
    def countDistance(self, p1, i, p2, s, c):
        if s[p1] is not c:
            return abs(p2 - i)
        elif s[p2] is not c:
            return abs(i - p1)
        else:
            left = abs(i - p1)
            right = abs(p2 - i)
            return left if left < right else right