class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        self.nums = nums
        self.res = 0
        self.record = {}
        return self.backtrack(n, 0, 0, target)
    
    def backtrack(self, n, idx, cur, target):
        # print(self.record)
        if cur == target and idx == n:
            return 1
        if idx == n:
            return 0
        key = str(idx) + " " + str(cur)
        if key in self.record:
            return self.record[key]
        a = self.backtrack(n, idx + 1, cur + self.nums[idx], target)
        b = self.backtrack(n, idx + 1, cur - self.nums[idx], target)
        self.record[key] = a + b
        return self.record[key]