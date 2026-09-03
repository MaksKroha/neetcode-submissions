# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs_with_max(node: TreeNode, curr_max_val: int):
            if node is None:
                return
            
            if node.val >= curr_max_val:
                nonlocal result 
                result += 1
                curr_max_val = node.val
            
            dfs_with_max(node.left, curr_max_val)
            dfs_with_max(node.right, curr_max_val)
        dfs_with_max(root, -101)
        return result