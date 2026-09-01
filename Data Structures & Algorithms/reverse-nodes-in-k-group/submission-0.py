# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode(0, None)
        previous_group_tail = result

        new_group_tail = head
        curr_node = head
        counter = 0
        
        while new_group_tail:
            prev_node = None
            curr_group_tail = new_group_tail
            while new_group_tail and counter < k:
                counter += 1
                new_group_tail = new_group_tail.next

            if counter == k:
                while counter > 0:
                    next_node = curr_node.next
                    curr_node.next = prev_node
                    prev_node = curr_node
                    curr_node = next_node
                    counter -= 1

                previous_group_tail.next = prev_node
                previous_group_tail = curr_group_tail
            else:
                previous_group_tail.next = curr_node
        return result.next


        


        
         
        