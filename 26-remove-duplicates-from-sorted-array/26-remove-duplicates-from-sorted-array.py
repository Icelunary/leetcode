class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeDown = 1
        # current = 1
        # current_max = nums[0]
        for i in range(1,len(nums)):
            # if nums[i] < current_max:
            #     print("Error")
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] > nums[i-1]:
                nums[writeDown] = nums[i]
                writeDown += 1
                # current_max = nums[i]
        # print(writeDown)
        # print(nums)
        return writeDown