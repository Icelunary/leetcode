class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mySet = set()
        # mySet.add(5)
        # print(mySet)
        cnt = 0
        for ele in arr:
            mySet.add(ele)
            if ele == 0:
                cnt += 1
        if cnt == 2: return True
        for ele in arr:
            if ele * 2 in mySet and ele != 0:
                return True