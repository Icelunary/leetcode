class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dis = math.inf
        res = -1
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums)-1
            while l < r:
                su = nums[i] + nums[l] + nums[r]
                cur = abs(su - target)
                if cur < dis:
                    dis = cur
                    res = su
                if not cur:
                    return su
                if su > target:
                    r -= 1
                else:
                    l += 1
        return res