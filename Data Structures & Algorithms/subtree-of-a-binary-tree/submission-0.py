# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
            if p is None:
                if q is None:
                    return True
                return False
            elif q is None:
                return False
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right and p.val == q.val
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

