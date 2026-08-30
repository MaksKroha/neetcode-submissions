# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(None, head)
        second = new_head
        node = new_head
        counter = 0

        while counter < n:
            counter += 1
            second = second.next
        
        while second.next:
            node = node.next
            second = second.next

        node.next = node.next.next
        return new_head.next

