class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.cnt = 1
        rightSteps = 0
        if abs(endPos - startPos) > k:
            return 0
        if (k - abs(endPos - startPos)) % 2 != 0:
            return 0
        else:
            rightStep = self.countRightStep(startPos, endPos, k)
        dis = k - rightStep
        test = 0
        print(k, rightStep, dis)
        # for i in range(k, rightStep, -1):
        #     self.cnt *= i
        for i in range(rightStep + 1, k + 1):
            self.cnt *= i

        for i in range(1, dis + 1):
            self.cnt //= i
        return self.cnt % (10 ** 9 + 7)
    
    def countRightStep(self, pos, endPos, k):
        if endPos >= pos:
            return endPos - pos + (k - (endPos - pos)) // 2
        else:
            return (k - (pos - endPos)) // 2