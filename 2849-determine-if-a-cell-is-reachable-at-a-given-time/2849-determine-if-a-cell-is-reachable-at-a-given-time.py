class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        xdif = abs(fx - sx)
        ydif = abs(fy - sy)
        mi = min(xdif, ydif) + abs(xdif - ydif)
        return t >= mi
        