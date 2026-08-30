# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        node_res = result 
        node1, node2 = l1, l2

        reminder = 0
        while node1 or node2:
            node1_val = node1.val if node1 else 0
            node2_val = node2.val if node2 else 0
            
            num = node1_val + node2_val + reminder
            
            addend = num % 10
            reminder = num // 10

            node_res.next = ListNode(addend, None)

            if node1:
                node1 = node1.next 
            if node2:
                node2 = node2.next
            node_res = node_res.next
        
        if reminder != 0:
            node_res.next = ListNode(reminder)
        return result.next



