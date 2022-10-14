class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        size = 0
        ma = -1
        stack = []
        for num in arr:
            if num > ma:
                ma = num
                stack.append(num)
                size += 1
            else:
                temp = stack[-1]
                while stack and num < stack[-1]:
                    stack.pop()
                    size -= 1
                stack.append(temp)
                size += 1
                

        return size