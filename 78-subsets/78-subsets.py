class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        n = len(nums)
        if n == 0:
            return self.res
        self.n = n
        self.nums = nums
        self.cur = []
        for i in range(n):
            self.backtrack(i)
        return self.res
        
    def backtrack(self, idx):
        if idx >= self.n:
            return
        self.cur.append(self.nums[idx])
        self.res.append(self.cur.copy())
        # print("append: ", self.cur)
        # print("after: ", self.res)
        for i in range(idx + 1, self.n):
            self.backtrack(i)

        self.cur.pop()
        