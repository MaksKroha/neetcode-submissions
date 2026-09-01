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
        counter = len(lists)
        while heap:
            smallest = heapq.heappop(heap)[2]
            node.next = smallest
            node = node.next

            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, counter, smallest.next))
                counter += 1
        return result.next
                    