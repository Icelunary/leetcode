import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.defaultdict(int)
        for word in words:
            cnt[word] += 1
        queue = []
        for word in cnt:
            heapq.heappush(queue, (-cnt[word], word))
        res = []
        for i in range(k):
            res.append(heapq.heappop(queue)[1])
        return res