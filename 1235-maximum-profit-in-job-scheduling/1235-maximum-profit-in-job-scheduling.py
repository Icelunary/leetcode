class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp1 = [] # for endTime
        dp2 = [] # for opt profit
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort(key = lambda x: x[0])
        # print("jobs", jobs)
        # tes = [1, 3, 5]
        # print(bisect.bisect_right(tes, 0) - 1)
        res = 0
        for job in jobs:
            if not dp1:
                dp1.append(job[0])
                dp2.append(job[2])
            else:
                idx = bisect.bisect_right(dp1, job[1]) - 1
                profit = job[2]
                if idx >= 0:
                    profit = profit = job[2] + dp2[idx]
                # if dp1[idx] <= job[1]:
                #     profit = job[2] + dp2[idx]
                if dp1[-1] == job[0]:
                    dp2[-1] = max(dp2[-1], profit)
                else:
                    dp1.append(job[0])
                    dp2.append(max(res, profit))
            res = max(res, dp2[-1])
        #     print(dp1)
        #     print(dp2)
        #     print()
        # print()
        # print(dp1)
        # print(dp2)
        return res