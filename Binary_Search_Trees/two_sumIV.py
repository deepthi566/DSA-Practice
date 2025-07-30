# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode],isReverse):
        self.stack = []
        self.reverse = isReverse
        self.push_all(root)
        

    def next(self) -> int:
        node = self.stack.pop()
        if not self.reverse:

            self.push_all(node.right)
        else:
            self.push_all(node.left)    
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def push_all(self,node):
        while node:
            self.stack.append(node)
            if not self.reverse:
            
                node = node.left
            else:
                node = node.right  
                  

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        l = BSTIterator(root,False)  
        r = BSTIterator(root,True)  

        i = l.next()
        j = r.next()
        while i<j:
            if i+j == k:
                return True
            elif i+j < k:
                i = l.next()
            else:
                j = r.next()        
        return False