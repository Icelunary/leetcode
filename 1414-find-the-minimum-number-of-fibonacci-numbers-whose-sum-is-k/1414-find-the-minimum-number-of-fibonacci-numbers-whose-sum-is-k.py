class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        # Lee's answer, better check discuss for great proof of greedy method
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res
    
        """ Below is my dp solution, TLE"""
        arr = [1, 1]
        while arr[-1] < k:
            arr.append(arr[-1] + arr[-2])
        n = len(arr)
        arr.reverse
        
        
        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        res = math.inf
        for idx in range(1, n + 1):
            # for i in dp:
            #     print(i)
            for total in range(1, k + 1):
                num = arr[idx - 1]
                if num < total:
                    if dp[idx - 1][total - num] != 0:
                        dp[idx][total] = 1 + dp[idx - 1][total - num]
                    else:
                        dp[idx][total] = dp[idx - 1][total]
                elif num == total:
                    dp[idx][total] = 1
                else:
                    dp[idx][total] = dp[idx - 1][total]

        return dp[n][k]