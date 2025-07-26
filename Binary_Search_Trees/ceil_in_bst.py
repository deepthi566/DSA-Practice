''' class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None '''
        
class Solution:
    def findCeil(self,root, inp):
        # code here
        ceil = -1
        while root:
            if root.key == inp:
                return root.key
            elif root.key < inp:
                root = root.right
            else:
                ceil = root.key
                root = root.left
        return ceil 