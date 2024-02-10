class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.checkCenter1(s, i, i)
            if i > 0:
                ans += self.checkCenter1(s, i - 1, i)
        
        return ans
        
    def checkCenter1(self, s: str, l: int, r: int) -> int:
        ans = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans
    