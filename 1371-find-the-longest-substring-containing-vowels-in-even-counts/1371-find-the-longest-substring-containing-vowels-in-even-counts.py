class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # From discussion
        seen = {0: -1}
        res = cur = 0
        for i, c in enumerate(s):
            # find the index of first time the situation appear
            cur ^= 1 << ('aeiou'.find(c) + 1) >> 1
            # record the situation and its index
            seen.setdefault(cur, i)
            # update max
            res = max(res, i - seen[cur])
        return res
            