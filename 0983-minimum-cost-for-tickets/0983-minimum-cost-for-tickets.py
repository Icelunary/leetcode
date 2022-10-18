class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [math.inf for i in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            day = days[i]
            choice1 = choice2 = choice3 = 0
            choice1 = dp[bisect.bisect_right(days, max(day - 1, 0))]
            choice2 = dp[bisect.bisect_right(days, max(day - 7, 0))]
            choice3 = dp[bisect.bisect_right(days, max(day - 30, 0))]
            # print(day, choice1, choice2, choice3)
            dp[i + 1] = min(choice1 + costs[0], choice2 + costs[1], choice3 + costs[2])
        #     print(dp)
        # print(dp)
        return dp[n]
        