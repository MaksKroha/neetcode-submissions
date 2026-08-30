"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_new = {None: None}

        node = head
        while node:
            original_new[node] = Node(node.val)
            node = node.next

        new_head = Node(0, None)
        new_curr_node = new_head
        curr_node = head
        while curr_node:
            new_node = original_new[curr_node]
            new_node.next = original_new[curr_node.next]
            new_node.random = original_new[curr_node.random]

            new_curr_node.next = new_node
            curr_node = curr_node.next
            new_curr_node = new_curr_node.next

        return new_head.next
