class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        look = "0"
        for c in s:
            if c != look:
                ans += 1
            if look == "0":
                look = "1"
            else:
                look = "0"
        
        return min(ans, len(s) - ans)