class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ziped = list(zip(heights, names))
        ziped.sort(key=lambda x: x[0])
        res = []
        for i in ziped:
            res.append(i[1])
        res.reverse()
        return res