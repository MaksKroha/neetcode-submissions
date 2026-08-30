# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        right = None
        while slow:
            curr_node = right
            right = slow
            slow = slow.next
            right.next = curr_node
        
        left = head
        while left:
            curr_next = left.next
            left.next = right
            right = right.next 
            left.next.next = curr_next 
            left = curr_next 