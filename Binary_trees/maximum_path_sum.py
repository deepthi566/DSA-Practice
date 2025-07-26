"""
maximum path sum
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def dfs(node):
            if not node:
                return 0
            lh = max(dfs(node.left),0)
            rh = max(dfs(node.right),0)
            curr = lh + rh + node.val
            self.maxi = max(self.maxi,curr)
            return node.val + max(lh,rh)
        dfs(root)    
        return self.maxi        

        