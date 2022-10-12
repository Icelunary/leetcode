import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        cnt = collections.defaultdict(int)
        for i in barcodes:
            cnt[i] += 1
        # print(cnt)
        res = []
        maxheap = []
        for k in cnt:
            heapq.heappush(maxheap, (-cnt[k], k))
        # print(maxheap)
        while len(res) < n:
            first = heapq.heappop(maxheap)
            # print("first", first)
            second = 0
            putback = 0
            if not res:
                res.append(first[1])
                putback = (first[0] + 1, first[1])
            else:
                if first[1] == res[-1]:
                    second = heapq.heappop(maxheap)
                    heapq.heappush(maxheap, first)
                    res.append(second[1])
                    putback = (second[0] + 1, second[1])
                else:
                    res.append(first[1])
                    putback = (first[0] + 1, first[1])
            heapq.heappush(maxheap, putback)
        #     print(res)
        # print(res)
        return res