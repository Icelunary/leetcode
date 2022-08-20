class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        myDic = {}
        target =  len(arr) // 2
        for i in arr:
            if i in myDic:
                myDic[i] += 1
            else:
                myDic[i] = 1
        print(myDic.values())
        sorted_list = sorted(list(myDic.values()), reverse = True)
        print(sorted_list)
        for i in range(len(sorted_list)):
            target -= sorted_list[i]
            if target <= 0:
                return i + 1
        