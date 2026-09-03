# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            nonlocal result
            if node is None:
                result.append("#")
            else:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        print(data)
        def dfs(idx) -> tuple[TreeNode, int]:
            nonlocal preorder
            if preorder[idx] == '#':
                return None, 1
            
            node = TreeNode(int(preorder[idx]))
            node.left, left_num = dfs(idx + 1)
            node.right, right_num = dfs(idx + 1 + left_num)
            return node, left_num + right_num + 1

        return dfs(0)[0]

