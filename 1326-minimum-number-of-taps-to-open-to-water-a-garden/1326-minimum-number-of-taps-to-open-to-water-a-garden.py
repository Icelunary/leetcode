class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
                
            left = i - ranges[i]
            right = i + ranges[i]
            intervals.append([left, right])
        intervals.sort(key=lambda x: (x[0], x[1]))
        # print(intervals)
        idx = 0
        uncover = 0
        tap = 0
        
        # we haven't cover all tap
        while uncover <= n:
            # current uncovered tap cannot be covered
            if idx >= len(intervals) or intervals[idx][0] > uncover:
                return -1
            
            l = r = uncover
            # find the furthest interval that can cover i
            while idx < len(intervals) and intervals[idx][0] <= uncover:
                l = min(l, intervals[idx][0])
                r = max(r, intervals[idx][1])
                idx += 1
                
            # in case the range is 0
            if l == r:
                return -1
            
            uncover = r
            tap += 1
            if r == n:
                return tap
        
        return tap