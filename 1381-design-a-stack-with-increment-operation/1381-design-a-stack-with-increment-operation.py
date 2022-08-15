class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.count = 0
        self.stack = []
        print("maxSize = ", self.maxSize)

    def push(self, x: int) -> None:
        if self.count < self.maxSize:
            self.stack.append(x)
            self.count += 1
        print(self.stack)

    def pop(self) -> int:
        if self.count > 0:
            self.count -= 1
            print(self.stack)
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        print(k, val, self.count)
        if k > self.count:
            self.increment(self.count, val)
        elif k > 0 and k <= self.count:
            for i in range(k):
                self.stack[i] += val
        print(self.stack)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)