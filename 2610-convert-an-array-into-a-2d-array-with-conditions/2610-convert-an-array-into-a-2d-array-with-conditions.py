class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        myMap = Counter(nums)
        ans = [[] for _ in range(max(myMap.values()))]
        mySet = set()
        nex = []
        for k in myMap:
            for num in range(myMap[k]):
                ans[num].append(k)
        return ans