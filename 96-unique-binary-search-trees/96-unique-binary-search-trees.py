class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n + 1):
            total = 0
            for j in range(i):
                total += dp[j] * dp[i - 1 - j]
            dp.append(total)
        return dp[n]