class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        elif n == 1:
            return s
        self.s = s
        self.max = 1
        self.res = s[0]
        for i in range(n):
            self.find(i, i, n)
            self.find(i, i+1, n)
        return self.res
        
    def find(self, l, r, n):
        while l >= 0 and r < n and self.s[l] == self.s[r]:
            l -= 1
            r += 1
        length = r - l - 1
        if length > self.max:
            self.max = length
            self.res = self.s[l+1: r]