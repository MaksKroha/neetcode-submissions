# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, array in enumerate(lists):
            if array:
                heapq.heappush(heap, (array.val, i, array))

        result = ListNode(0, None)
        node = result
        while heap:
            _, i, smallest = heapq.heappop(heap)
            node.next = smallest
            node = node.next

            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, i, smallest.next))
        return result.next
                    