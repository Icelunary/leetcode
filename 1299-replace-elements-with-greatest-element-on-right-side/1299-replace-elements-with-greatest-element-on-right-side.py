class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pre = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > pre:
                arr[i], pre = pre, arr[i]
            else:
                arr[i] = pre
        
        return arr