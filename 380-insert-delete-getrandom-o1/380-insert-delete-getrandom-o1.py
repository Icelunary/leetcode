import random
class RandomizedSet:

    def __init__(self):
        self.myList = []
        self.myMap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.myMap:
            self.myList.append(val)
            self.myMap[val] = self.length
            self.length += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.myMap:
            index = self.myMap[val]
            self.myList[index] = self.myList[-1]
            self.myMap[self.myList[-1]] = index
            del self.myMap[val]
            self.myList.pop()
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        if self.myMap:
            index = random.randint(0, self.length - 1)
            return self.myList[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()