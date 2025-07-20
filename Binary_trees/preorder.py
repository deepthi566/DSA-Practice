"""

preorder traversal



"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preOrder = []
        stack = [root]
        while stack:
            node = stack.pop()
            preOrder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preOrder            
