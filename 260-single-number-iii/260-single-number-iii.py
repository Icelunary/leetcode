class Solution:
    def singleNumber(self, nums):
        # from discuss
        # https://blog.csdn.net/oyoung_2012/article/details/79932394
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)
        