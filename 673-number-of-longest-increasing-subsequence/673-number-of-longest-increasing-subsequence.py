class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = 0
        cnt = 1
        deck = [math.inf]
        decks = [[]]
        ways = [[]]
        for i in range(len(nums)):
            num = nums[i]
            idx = 0
            idx_sum = 0
            if deck[-1] < num:
                # print("case1")
                deck.append(num)
                decks.append([num])
                ways.append([])
                idx = maxLen
                maxLen += 1
                idx_sum = maxLen
                cnt += 1               
            else:
                # print("case2")
                idx = bisect_left(deck, num)
                deck[idx] = num
                idx_sum = idx
                decks[idx].append(num)
                idx -= 1
            end = bisect_left(decks[idx][::-1], num)
            if idx_sum == 0:
                ways[idx_sum].append(1)
            else:
                ways[idx_sum].append(sum(ways[idx][::-1][:end]))
#             print(ways)
#             print()
                
#         print("final")
#         print(deck)
#         print(decks)
#         print(ways)
        return sum(ways[-1])