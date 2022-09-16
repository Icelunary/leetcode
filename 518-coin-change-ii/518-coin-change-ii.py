class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if amount == 0:
            return 1
        dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]
        for r in range(1, n + 1):
            for k in range(1, amount + 1):
                coin = coins[r-1]
                if coin == k:
                    dp[r][k] = 1 + dp[r-1][k]
                elif coin > k:
                    dp[r][k] = dp[r-1][k]
                else:
                    dp[r][k] = dp[r-1][k] + dp[r][k-coin]
        return dp[n][amount]