class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        if not n or not m:
            return 0
        # dp[i][j] means the max common sub arrays ending in i and j
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        res = 0
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if nums1[r-1] == nums2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                    res = max(res, dp[r][c])

        return res