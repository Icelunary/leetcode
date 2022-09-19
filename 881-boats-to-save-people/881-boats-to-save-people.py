class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        n = len(people)
        r = n - 1 - l
        cnt = 0
        left = limit
        while l <= r:
            if people[r] <= left:
                left -= people[r]
                if people[l] <= left:
                    left -= people[l]
                    l += 1
                r -= 1
            left = limit
            cnt += 1
        return cnt
        