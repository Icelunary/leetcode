class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        myDict = defaultdict(int)
        # print(myDict[0])
        ret = 0
        for num in arr:
            myDict[num] = max(myDict[num], myDict[num-difference] + 1)
            ret = max(ret, myDict[num])
            # print(ret, myDict, num, num+difference, num-difference)
        return ret