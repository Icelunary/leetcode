class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =  nums
#         self.dp = self.construct_dp()

#     def construct_dp(self):
#         dp = []
#         length = len(self.nums)
#         for i in range(length):
#             dp.append([])
#             for j in range(i):
#                 dp[i].append(0)
#         for i in range(length):
#             dp[i].append(self.nums[i])
#             for j in range(i+1, length):
#                 dp[i].append(dp[i][j-1] + self.nums[j])
#         return dp
        
    def sumRange(self, left: int, right: int) -> int:
        my_sum = 0
        for i in range(left, right+1):
            my_sum += self.nums[i]
        return my_sum
        # return self.dp[left][right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)