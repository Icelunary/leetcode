class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        # lee's solution QAQ
        res, s1, s2 = [-1] * len(A), [], []
        for i,a in enumerate(A):
            while s2 and A[s2[-1]] < a:
                res[s2.pop()] = a;
            tmp = []
            while s1 and A[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res
    
        # WA
        stack = deque([])
        stackRecords = {}
        # ma =[-1 for i in range(len(nums))]
        # for i in range(len(nums)-2, -1, -1):
        #     ma[i] = max(ma[i+1], nums[i+1])
        # print(ma)
        
        for i in range(len(nums)):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                stackRecords[stack.pop()] = i
            stack.append(i)
        #     print(stack)
        print(stackRecords)
        stack = []
        secondRecords = {}
        for i in range(len(nums)):
            num = nums[i]
            while stack and nums[stack[-1]] <= num:
                secondRecords[stack.pop()] = num
            stack.append(i)
        print(secondRecords)
        res = []
        for i in range(len(nums)):
            if i in stackRecords and stackRecords[i] in secondRecords:
                res.append(secondRecords[stackRecords[i]])
            else:
                res.append(-1)
        
        return res
    
    
        # WA
        head = nums[-1]
        mid = nums[-2]
        res = []
        for i in range(len(nums)-1-2, -1, -1):
            num = nums[i]
            print(num, mid, head)
            if head != -1 and mid != math.inf and num < mid and num < head:
                res.append(head)
            else:
                res.append(-1)
            if head == -1:
                head = num
            else:
                if num >= head:
                    head = num
                elif num > tail:
                    mid = num
        print(res)
        return reversed(res)