class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 0
        for num in arr:
            if num - difference in dp:
                dp[num] = 1 + dp[num - difference]
            else:
                dp[num] = 1
            res = max(res, dp[num])
        return res