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
    
"""From discuss, it's actually the same but mine code look worse
def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
"""