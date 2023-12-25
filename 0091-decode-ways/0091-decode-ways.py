class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0,] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        if s[0] == "0":
            return 0
        
        for i in range(1, len(s)):
            if s[i] == "0" and s[i-1] == "0":
                # print("break at ", i)
                dp[-1] = 0
                break
            l = int(s[i - 1])
            r = int(s[i])
            if l > 0 and l * 10 + r <= 26:
                dp[i + 1] += dp[i - 1]
            if r != 0:
                dp[i + 1] += dp[i]
        return dp[len(s)]