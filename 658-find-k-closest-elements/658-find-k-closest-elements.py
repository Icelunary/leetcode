class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis = []
        n = len(arr)
        for i in range(n):
            dis.append((abs(x - arr[i]), i))
        dis = sorted(dis, key=lambda x: (x[0],x[1]))
        res = []
        for ele in dis[:k]:
            res.append(arr[ele[1]])
        res.sort()
        return res