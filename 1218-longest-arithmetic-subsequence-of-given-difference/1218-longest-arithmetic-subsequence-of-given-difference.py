class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        myDict = defaultdict(int)
        # print(myDict[0])
        ret = 0
        for i in range(n-1,0-1, -1):
            num = arr[i]
            myDict[num] = max(myDict[num], myDict[num+difference] + 1)
            ret = max(ret, myDict[num])
            # print(ret, myDict, num, num+difference, num-difference)
        return ret