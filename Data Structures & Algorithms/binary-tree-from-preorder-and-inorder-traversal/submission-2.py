# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build_and_get_elements(min_idx, max_idx, preorder_idx):
            nonlocal inorder_map, preorder 
            if max_idx - min_idx == 0:
                return None, 0
            if max_idx - min_idx == 1:
                return TreeNode(preorder[preorder_idx]), 1

            node = TreeNode(preorder[preorder_idx])
            inorder_idx = inorder_map[preorder[preorder_idx]]

            node.left, left_el_num = build_and_get_elements(
                min_idx, inorder_idx, preorder_idx + 1 
            )
            node.right, right_el_num = build_and_get_elements(
                inorder_idx + 1, max_idx, 
                preorder_idx + left_el_num + 1
            )
            return node, left_el_num + right_el_num + 1
        return build_and_get_elements(0, len(inorder), 0)[0]
