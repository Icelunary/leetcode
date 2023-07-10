class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        m = len(moveFrom)
        n = len(nums)
        # print("round")
        # print(nums)
        ret = set(nums)
        print(ret)
        for i in range(m):
            move = moveFrom[i]
            to = moveTo[i]
            ret.remove(move)
            ret.add(to)
        ret = list(ret)
        ret.sort()
        print(ret)
        return ret

        # m = len(moveFrom)
        # n = len(nums)
        # # print("round")
        # # print(nums)
        # moveDic = dict()
        # for i in range(m):
        #     if i in moveDic.keys():
        #         moveDic