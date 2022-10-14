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