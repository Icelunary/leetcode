class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        cnt = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                cnt += 1
            
        if cnt > 1:
            product = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                ans[i] = product
            else:
                ans[i] = product // nums[i]
                if cnt > 0:
                    ans[i] = 0
        return ans