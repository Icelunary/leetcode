class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi = -math.inf
        ma = -math.inf
        record = math.inf
        for num in nums:
            if num > record:
                return True
            if mi == -math.inf:
                mi = ma = num
            elif num > ma:
                if ma != mi:
                    return True
                else:
                    ma = num
                    record = min(record, ma)
            elif num < mi:
                mi = ma = num
            if num > mi:
                record = min(record, num)
            # print(mi, ma, record)
        return False