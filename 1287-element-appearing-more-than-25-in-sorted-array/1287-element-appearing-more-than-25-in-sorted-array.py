class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n//4
        record = Counter(arr)
        for num in record:
            if record[num] > target:
                return num
            