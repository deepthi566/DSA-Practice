# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, minv, maxv):
            if not root:
                return True
            if root.val <= minv or root.val >= maxv:
                return False
            return validate(root.left, minv, root.val) and validate(root.right, root.val, maxv)
        
        return validate(root, float('-inf'), float('inf'))
            