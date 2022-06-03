class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =  nums
        self.dp = self.construct_dp()

    def construct_dp(self):
        dp = []
        length = len(self.nums)
        dp.append(self.nums[0])
        for i in range(1, length):
            dp.append(dp[i-1] + self.nums[i])
        return dp
        
    def sumRange(self, left: int, right: int) -> int:
        # my_sum = 0
        # for i in range(left, right+1):
        #     my_sum += self.nums[i]
        # return my_sum
        if left == 0:
            return self.dp[right]
        else:
            return self.dp[right] - self.dp[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)