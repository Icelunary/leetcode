class Solution:
    # from submission
    def numSquares(self, n):
        if int(n**(1/2))**2 == n:
            return 1
        for i in range(int(n**(1/2))+1):
            if int((n - i**2)**(1/2))**2 == n-i**2:
                return 2
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        else:
            return 3