# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return False
            
        slow_pointer = head
        quick_pointer = head

        while quick_pointer.next and quick_pointer.next.next:
            slow_pointer = slow_pointer.next
            quick_pointer = quick_pointer.next.next

            if slow_pointer == quick_pointer:
                return True
        return False