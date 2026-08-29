# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            return_list1 = True
            node1, node2 = list1, list2
        else:
            return_list1 = False
            node1, node2 = list2, list1

        while node1.next:
            if node2 and node1.next.val > node2.val:
                node1.next = ListNode(node2.val, node1.next)
                node2 = node2.next
            node1 = node1.next
        node1.next = node2
        return list1 if return_list1 else list2
        