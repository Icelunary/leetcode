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
        print(intervals)
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
                
            print([l, r])
            # in case the range is 0
            if l == r:
                return -1
            
            uncover = r
            tap += 1
            if r == n:
                return tap
        
        return tap
            
        for i in range(n):
            # i is already covered
            if i < uncover:
                continue
                
            # i cannot be covered
            if idx >= len(intervals) or intervals[idx][0] > i:
                return -1
            
            # find the furthest interval that can cover i
            rightMost = i
            while idx < len(intervals) and intervals[idx][0] <= i:
                idx += 1
                rightMost = max(rightMost, intervals[idx][1])
            print(idx, i)
            # record covered tap
            if intervals[idx-1][1] == intervals[idx-1][0]:
                print(uncover, i, idx)
                print()
                print(intervals[idx-1])
                return -1
            
            uncover = intervals[idx-1][1] + 1
            tap += 1
            
        return tap