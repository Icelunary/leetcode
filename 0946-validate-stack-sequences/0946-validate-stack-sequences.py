class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        nex = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[nex]:
                stack.pop()
                nex += 1
                if nex == len(popped):
                    return True
        return False