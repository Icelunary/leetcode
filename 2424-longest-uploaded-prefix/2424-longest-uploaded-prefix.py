class LUPrefix:

    def __init__(self, n: int):
        self.videos = [0 for i in range(n)]
        self.size = n
        self.fa = list(range(n))
        # print(self.fa)

    def upload(self, video: int) -> None:
        self.videos[video-1] = 1
        if video != self.size:
            self.fa[self.find(video-1)] = self.find(video)
            # print(self.fa)

    def longest(self) -> int:
        if self.videos[0] == 0:
            return 0
        else:
            end = self.find(0)
            # print("finding", self.fa)
            if self.videos[end] == 1:
                return end + 1
            else:
                return end
    
    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()