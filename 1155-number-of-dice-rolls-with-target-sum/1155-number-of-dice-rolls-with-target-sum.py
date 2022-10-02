class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0
        self.cnt = 0
        self.dp = {}
        return self.track(n, k, target) % (pow(10, 9) + 7)
    
    def track(self, n, k, target):
        if n == 0:
            if target == 0:
                self.dp[(n, target)] = 1
                return 1
            else:
                self.dp[(n, target)] = 0
                return 0
        if target <= 0:
            self.dp[(n, target)] = 0
            return 0
        if (n, target) in self.dp:
            return self.dp[(n, target)]
        temp = 0
        for i in range(1, k + 1):
            temp += self.track(n-1, k, target - i)
            # print(self.dp, temp)
        self.dp[(n, target)] = temp
        # print("this is", self.dp)
        return temp