
"""
postorder traversal



"""

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res = []
        current = root
        last_visited = None
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    res.append(peek_node.val)
                    last_visited = stack.pop()   
        return res             


        