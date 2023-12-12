class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/3983936/3-Minutes-To-Realise-Greedy-Approach-Beats-99
        # thanks to mchlkrpch's solution in discussion
        # following solution is inspired by him/her
        arr = [0] * (n + 1)
        ans = 0
        
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            arr[left] = max(right, arr[left])
        # print(arr)
        pre = 0
        uncover = 0
        while uncover < n:
            nex = 0
            for i in range(pre, uncover + 1):
                # print(i, arr[i],  "uncover: ", uncover, max(uncover, arr[i]))
                nex = max(nex, arr[i])
            # print(pre, uncover, nex)
            if nex <= uncover:
                return -1
            pre, uncover = uncover + 1, nex
                
            ans += 1
            
        return ans
        
        
        # my solution
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
        while uncover < n:
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
        
        return tap