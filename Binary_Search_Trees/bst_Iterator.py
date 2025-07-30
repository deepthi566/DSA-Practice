# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_all(root)
        

    def next(self) -> int:
        node = self.stack.pop()
        self.push_all(node.right)
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def push_all(self,node):
        while node:
            self.stack.append(node)
            node = node.left