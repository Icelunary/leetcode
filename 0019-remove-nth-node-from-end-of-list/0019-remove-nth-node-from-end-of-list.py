# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        root = head
        while root:
            length += 1
            root = root.next
            
        root = head
        if length == n:
            return head.next
        
        while length != n + 1:
            root = root.next
            length -= 1
        
        root.next = root.next.next
            
        return head