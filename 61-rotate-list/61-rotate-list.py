# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        length_count = 1
        current_node = head
        while current_node.next is not None:
            length_count += 1
            current_node = current_node.next
        
        # print(length_count)
        last_node = current_node
        last_node.next = head
        current_node = head
        # print(k%length_count)
        dis = length_count - (k % length_count) - 1
        # print(dis)
        for i in range(dis):
            current_node = current_node.next
        new_head = current_node.next
        current_node.next = None
        return new_head
        