class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        preSum = [0 for i in range(n)]
        for (first, last, seats) in bookings:
            preSum[first - 1] += seats
            if last - 1 < n - 1:
                preSum[last] -= seats
        res = [preSum[0]]
        for idx in range(1, len(preSum)):
            res.append(preSum[idx] + res[idx-1])
        return res
        