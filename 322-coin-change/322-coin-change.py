class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if amount == 0:
            return 0
        dp = [[math.inf for i in range(amount + 1)] for j in range(n + 1)]
        for r in range(1, n + 1):
            for c in range(1, amount + 1):
                if coins[r-1] == c:
                    dp[r][c] = 1
                elif coins[r-1] < c:
                    dp[r][c] = min(dp[r-1][c-coins[r-1]] + 1, dp[r-1][c], dp[r][c-coins[r-1]] + 1)
                elif coins[r-1] > c:
                    dp[r][c] = dp[r-1][c]
        if dp[n][amount] == math.inf:
            return -1
        return dp[n][amount]