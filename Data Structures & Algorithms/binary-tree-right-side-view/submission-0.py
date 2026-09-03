# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def check_view(node: Optional[TreeNode], curr_level: int):
            if node is None:
                return
            
            nonlocal result
            if len(result) < curr_level:
                result.append(node.val)
            
            check_view(node.right, curr_level + 1)
            check_view(node.left, curr_level + 1)
        check_view(root, 1)
        return result