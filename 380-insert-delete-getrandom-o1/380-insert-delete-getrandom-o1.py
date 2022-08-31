from random import sample
class RandomizedSet:

    def __init__(self):
        self.mySet = set()

    def insert(self, val: int) -> bool:
        if val not in self.mySet:
            self.mySet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.mySet:
            self.mySet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if self.mySet:
            return sample(self.mySet, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()