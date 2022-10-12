class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        ma = sum(nums[l:r])
        cur = ma
        # print(ma)
        while r < len(nums):
            # print("add", nums[r], "remove", nums[l])
            cur += nums[r] - nums[l]
            # print(cur)
            l += 1
            r += 1
            ma = max(ma, cur)
        return ma / k