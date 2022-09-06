class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:     
        self.res = [0, cost[0], cost[1]]
        self.dp(cost)
        return min(self.res[-1], self.res[-2])
    
    def dp(self, cost):
        n = len(cost)
        for i in range(2, n):
            self.res.append(min(self.res[i] + cost[i], self.res[i-1] + cost[i]))
            