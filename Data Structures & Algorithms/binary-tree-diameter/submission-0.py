# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def most_distant_node(node: Optional[TreeNode]):
            if node is None:
                return 0

            left_most_distant = most_distant_node(node.left)
            right_most_distant = most_distant_node(node.right)
            
            nonlocal max_diameter
            max_diameter = max(max_diameter, left_most_distant + right_most_distant)
            return max(left_most_distant, right_most_distant) + 1
        most_distant_node(root)
        return max_diameter