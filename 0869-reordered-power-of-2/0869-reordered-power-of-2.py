class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        leng = len(str(n))
        compares = []
        tot = 1
        while len(str(tot)) < leng + 1:
            if len(str(tot)) == leng:
                compares.append(tot)
            tot *= 2
        # print(compares)
        for num in compares:
            if Counter(str(n)) == Counter(str(num)):
                return True
        return False
    
    
    def compare(self, a, b: str) -> bool:
        return Counter(a) == Counter(b)