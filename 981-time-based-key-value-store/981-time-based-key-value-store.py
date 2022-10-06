class TimeMap:

    def __init__(self):
        self.timestamp = {}
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp:
            self.timestamp[key] = [[timestamp, value]]
            self.keys[key] = [timestamp]
        else:
            self.timestamp[key].append([timestamp, value])
            self.keys[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timestamp:
            return self.find(self.keys[key], timestamp, key)
        else:
            return ""
    
    def find(self, myMap: list, timestamp: int, key:str) -> str:
        idx = bisect.bisect(myMap, timestamp)
        return "" if idx == 0 else self.timestamp[key][idx-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)