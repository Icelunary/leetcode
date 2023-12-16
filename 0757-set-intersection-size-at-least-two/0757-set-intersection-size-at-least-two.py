# class Solution:
#     def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
#         start = sorted(intervals, key=lambda x: x[0])
#         ends = sorted(intervals, key=lambda x: x[1])
#         nodeSet = set()
#         adjListEnd = defaultdict(list) # pointing to the end
#         adjListStart = defaultdict(list) # pointing to the start
#         cnt = defaultdict(int)
#         for i, j in intervals:
#             nodeSet.add(i)
#             nodeSet.add(j)
#             adjListEnd[i].append(j)
#             adjListStart[j].append(i)
#             cnt[(i, j)] = 0
        
#         nodes = sorted(list(nodeSet))
        
#         ans = 0
#         print(nodes)
#         print(adjListEnd)
#         print(adjListStart)
#         print(cnt)
#         overlap = deque([])
#         # test = [1,2,3]
#         # overlap += test
#         # print(overlap)
#         for node in nodes:
#             if node in adjListStart:
#                 mi = 2
#                 for s inadjListStart
#                 num = 2 - cnt[node]
#                 ans += num
#                 while overlap:
#                     cur = overlap.pop()
#                     endNode = adjListEnd[cur]
                    
#             overlap += adjListEnd[node]

#         return ans
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/2700915/Python-Explained-or-O(nlogn)
        # The orginal explaination is not enough for me, here is my explaination
        # If we encounter a intervals, we must finish this interval's requirement
        # We'll record the interval that cover last two nums, which means, for [l, r], we select l, r 
        # For current interval, if they do not overlap with last [l, r], we select [cur_r-1, cur_r] as new cover
        
        # If overlap, if cur_l <= pre_l, current interval is satisfied. Skip it
        #                                because we have selected pre_l and pre_r
        # Then select new pre l and pre r. New pre R is always current r
        # For new pre_l, if they overlap but not having the same end, 
        # we already have 1 num in pre_r, so we select another num in cur_R
        # If they have the same end, for example
        # [2,7] [5,7]. We already have num in 2 and 7, so we select curr_end and curr_end -1
        intervals.sort(key = lambda x:x[1])
        size = 0
        prev_start = -1
        prev_end = -1
        # the first one is always not overlap case
        # second one is always edge to edge
        for curr_start, curr_end in intervals:
            if prev_start == -1 or prev_end < curr_start: #if intervals do not overlap
                size += 2
                prev_start = curr_end-1
                prev_end = curr_end

            elif prev_start < curr_start: #if intervals overlap
                if prev_end != curr_end:
                    prev_start = prev_end
                    prev_end = curr_end
                    
                else:
                    prev_start = curr_end-1
                    prev_end = curr_end

                size += 1

        return size