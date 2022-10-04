class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        total = []
        for k in cnt:
            total.append([k, k * cnt[k]])
        total.sort(key = lambda x: x[0])
        dp = []
        res = 0
        for i in range(len(total)):
            if not dp:
                dp.append(total[i][1])
            elif i == 1:
                if total[i][0] == total[i-1][0] + 1:
                    dp.append(max(total[i][1], dp[-1]))
                else:
                    dp.append(dp[-1] + total[i][1])
            else:
                if total[i][0] == total[i-1][0] + 1:
                    dp.append(max(dp[-2] + total[i][1], dp[-1]))
                else:
                    dp.append(dp[-1] + total[i][1])
        return dp[-1]