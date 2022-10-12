class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        a1 = nums[0]
        a2 = nums[1]
        a3 = nums[2]
        if self.check(a1, a2, a3):
            return sum([a1, a2, a3])
        for num in nums[3:]:
            a1 = a2
            a2 = a3
            a3 = num
            if self.check(a1, a2, a3):
                return sum([a1, a2, a3])
        return 0
                
    
    def check(self, a1, a2, a3: int) -> bool:
        if a1 + a2 > a3 and a2 + a3 > a1 and a1 + a3 > a2:
            return True
        else:
            return False