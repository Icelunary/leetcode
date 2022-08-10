class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length - 1
        mid = 0
        while start < end:
            mid = (start + end) // 2
            # print(mid)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                # print("case0")
                return mid
        if nums[start] < target:
            # print("case2")
            return start+1
        else:
            return start