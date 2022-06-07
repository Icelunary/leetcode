# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        travel1 = headA
        travel2 = headB
        switch = 0
        while travel1 is not None:
            # print()
            # print(travel1.val, travel2.val)
            if travel1 == travel2:
                return travel1
            travel1 = travel1.next
            travel2 = travel2.next
            # print(travel1, travel2)
            
            
            
            if travel1 == None and switch < 2:
                travel1 = headB
                switch += 1
                # print("switch 1")
            if travel2 == None and switch < 2:
                travel2 = headA
                switch += 1
                # print("switch 2")
            # if travel1 == travel2:
            #     # print("done")
            #     return travel1
            # print(travel1.val, travel2.val)
        return travel1