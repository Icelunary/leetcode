class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = r = 0
        ans = 0
        while r < len(s) and l < len(g):
            if s[r] >= g[l]:
                ans += 1
                l += 1
            r += 1
        return ans