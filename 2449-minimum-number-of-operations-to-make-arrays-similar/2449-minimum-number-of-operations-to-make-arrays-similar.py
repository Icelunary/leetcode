class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = sum(target)
        if sum1 != sum2:
            return False
        myEvens = []
        myOdds = []
        for num in nums:
            if num % 2 == 0:
                myEvens.append(num)
            else:
                myOdds.append(num)
        target.sort()
        myEvens.sort()
        myOdds.sort()
        myEvens.reverse()
        myOdds.reverse()
        target.reverse()
        l = r = 0
        cnt = 0
        idx = 0
        for i in range(len(nums)):
            num = target[i]
            if num % 2 == 0:
                # print(num, myEvens[r])
                cnt += abs(num - myEvens[r]) // 2
                r += 1
            else:
                # print(num, myOdds[r])
                cnt += abs(num - myOdds[l]) // 2
                l += 1
        return cnt // 2
