class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        preSums = [0] * n
        preSum = 0
        for i in range(n):
            preSum += preSums[i]
            nums[i] -= preSum
            if nums[i] < 0:
                return False
            preSum += nums[i]
            if i + k < n:
                preSums[i+k] -= nums[i]
            if i + k - 1 < n:
                nums[i] = 0
        return nums[-1] == 0