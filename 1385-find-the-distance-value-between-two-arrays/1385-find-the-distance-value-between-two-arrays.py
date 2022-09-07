class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr1)
        m = len(arr2)
        self.res = n
        arr2.sort()
        for target in arr1:
            self.bs(arr2, 0, m - 1, target, d)
        return self.res
        
    def bs(self, arr2, start, end, target, d):
        if end >= start:
            mid = (start + end) // 2
            num = arr2[mid]
            dis = abs(num - target)
            if dis <= d:
                self.res -= 1
                return
            if num > target:
                return self.bs(arr2, start, mid - 1, target, d)
            elif num < target:
                return self.bs(arr2, mid + 1, end, target, d)