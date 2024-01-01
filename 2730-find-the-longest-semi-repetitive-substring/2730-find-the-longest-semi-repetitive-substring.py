class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        repeat = False
        # "0001"
        l, r = 0, 1
        while r < len(s):
            if s[r] == s[r - 1]:
                while repeat:
                    l += 1
                    if s[l] == s[l - 1]:
                        repeat = False
                repeat = True
            r += 1
            ans = max(r - l, ans)
        
        return max(ans, len(s) - l)
                