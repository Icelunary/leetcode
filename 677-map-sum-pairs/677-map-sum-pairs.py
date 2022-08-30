class MapSum:

    def __init__(self):
        self.sums = {}
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.map:
            dif = val - self.map[key]
            self.map[key] = val
            self.update_val(key, dif)
        else:
            self.map[key] = val
            self.update_val(key, val)
            
    def update_val(self, key, val) -> None:
        for i in range(1, len(key) + 1):
            if key[:i] in self.sums:    
                self.sums[key[:i]] += val
            else:
                # print(self.map, key[:i])
                self.sums[key[:i]] = val

    def sum(self, prefix: str) -> int:
        return self.sums[prefix] if prefix in self.sums else 0



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)