
"""

inorder traversal

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder  = []
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)    
        return inorder