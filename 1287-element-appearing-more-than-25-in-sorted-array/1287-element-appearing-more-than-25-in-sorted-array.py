class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n//4
        cnt = 0
        for i in range(len(arr)):
            if i == 0:
                cnt += 1
            else:
                if arr[i] == arr[i-1]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > target:
                    return arr[i]
        
        # Old version
        n = len(arr)
        target = n//4
        record = Counter(arr)
        for num in record:
            if record[num] > target:
                return num
            