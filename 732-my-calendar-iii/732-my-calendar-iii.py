class MyCalendarThree:

    def __init__(self):
        self.books = []
        self.booke = []
        self.n = 0

    def book(self, start: int, end: int) -> int:
        self.books.append(start)
        self.booke.append(end)
        self.n += 1
        # print("getMax from", start, end)
        return self.getMax()
    
    def getMax(self):
        l = r = 0
        ma = 0
        cnt = 0
        cur = -1
        self.books.sort()
        self.booke.sort()
        while l < self.n:
            while l < self.n and self.booke[r] > self.books[l]:
                # print("+1: ", self.books[l], self.booke[r], self.books, self.booke)
                cnt += 1
                ma = max(ma, cnt)
                l += 1
            # print("over")
            cnt -= 1
            r += 1
        return ma
            


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)