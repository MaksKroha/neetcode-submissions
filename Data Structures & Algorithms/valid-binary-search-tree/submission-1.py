# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_with_range(node: Optional[TreeNode], min_val: int, max_val: int):
            if node is None:
                return True
            
            if not node.val > min_val or not node.val < max_val:
                return False
            
            return (
                dfs_with_range(node.left, min_val, node.val) and
                dfs_with_range(node.right, node.val, max_val)
            )
        return dfs_with_range(root, -1000000001, 1000000001)