class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        trunks = [] # Each element presents corresponding trunk's max value
        current_max = None
        trunk_nums = 0
        for ele in arr:
            if current_max == None or ele >= current_max:
                trunks.append(ele)
                current_max = ele
                trunk_nums += 1
            currentIndex = trunk_nums - 1
            # print(currentIndex, trunk_nums, trunks)
            if ele < trunks[currentIndex] and trunk_nums > 1:
                trunk_nums, current_max = self.mergeTrunk(trunks, trunk_nums, ele, current_max)
        return trunk_nums
    
    
    def mergeTrunk(self, trunks, trunk_nums, ele, current_max):
        preTrunkIndex =  trunk_nums - 2
        if preTrunkIndex >= 0 and trunks[preTrunkIndex] > ele:
            current_max = trunks[trunk_nums - 1]
            trunks[preTrunkIndex] = current_max
            del trunks[trunk_nums - 1]
            trunk_nums -= 1
            return self.mergeTrunk(trunks, trunk_nums, ele, current_max)
        return trunk_nums, current_max
            