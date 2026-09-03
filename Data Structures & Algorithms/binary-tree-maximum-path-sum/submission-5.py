# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -1001

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -1001

            left_max_path = dfs(node.left)
            right_max_path = dfs(node.right)

            nonlocal max_path_sum
            max_path_sum = max(
                max_path_sum,
                left_max_path,
                right_max_path,
                left_max_path + right_max_path + node.val,
                right_max_path + node.val,
                left_max_path + node.val,
                node.val
            )
            return max(
                left_max_path + node.val,
                right_max_path + node.val,
                node.val
            )
        dfs(root)
        return max_path_sum