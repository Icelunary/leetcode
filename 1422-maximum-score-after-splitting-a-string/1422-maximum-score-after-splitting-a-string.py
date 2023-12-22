class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        num0 = [0 for  _ in range(n + 1)]
        num1 = [0 for _ in range(n + 1)]
        for i in range(n):
            if s[i] == "0":
                num0[i + 1] = 1 + num0[i]
                num1[i + 1] = num1[i]
            else:
                num0[i + 1] = num0[i]
                num1[i + 1] = 1 + num1[i]
        ans = 0
        for i in range(1, n):
            cur = num0[i] + num1[-1] - num1[i]
            ans = max(ans, cur)
        return ans