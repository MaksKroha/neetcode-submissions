# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def get_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            if abs(left_height - right_height) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(left_height, right_height) + 1
        get_height(root)
        return is_balanced