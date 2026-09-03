# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def in_order(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            in_order(node.left)
            nonlocal arr
            arr.append(node.val)
            in_order(node.right)
        in_order(root)
        return arr[k - 1]


