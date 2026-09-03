# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val:
            p_next_node = root.left
        else:
            p_next_node = root.right
        
        if q.val < root.val:
            q_next_node = root.left
        else:
            q_next_node = root.right
        
        if q_next_node.val != p_next_node.val:
            return root
        return self.lowestCommonAncestor(q_next_node, p, q)