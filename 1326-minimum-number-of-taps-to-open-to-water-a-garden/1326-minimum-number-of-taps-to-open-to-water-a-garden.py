class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n + 1)
        for idx, cur_radius in enumerate(ranges):
            if cur_radius == 0:
                continue
            
            left_border_idx = max(0, idx - cur_radius)
            arr[left_border_idx] = max(arr[left_border_idx], idx + cur_radius)

        right_border_of_watered_points = 0
        ans, watered_on_cur_step = 0, 0

        for idx, right_border in enumerate(arr):
            if idx > watered_on_cur_step:
                if right_border_of_watered_points <= watered_on_cur_step:
                    return -1
                ans += 1
                watered_on_cur_step = right_border_of_watered_points

            right_border_of_watered_points = max(right_border_of_watered_points, right_border)

        return ans + (watered_on_cur_step < n)
        
        
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