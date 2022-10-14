# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        first = head
        second = head.next
        go = True
        while go:
            if second.next and second.next.next:
                second = second.next.next
                first = first.next
            else:
                if first.next.next:
                    first.next = first.next.next
                else:
                    first.next = None
                go = False
        return head
    
    """ from discuss
        def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = slow = fast = ListNode(-math.inf)
        dummy.next = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next    
        return dummy.next
        """