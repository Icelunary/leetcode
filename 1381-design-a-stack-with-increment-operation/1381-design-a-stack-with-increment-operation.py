class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.count = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.count < self.maxSize:
            self.stack.append(x)
            self.count += 1

    def pop(self) -> int:
        if self.count > 0:
            self.count -= 1
            ele = self.stack[-1]
            del self.stack[-1]
            return ele
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        print(k, val, self.count)
        if k > self.count:
            self.increment(self.count, val)
        elif k > 0 and k <= self.count:
            for i in range(k):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)