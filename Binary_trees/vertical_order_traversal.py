from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root,0,0)])
        level_list=[]
        while queue:
            node,col,row = queue.popleft()
            level_list.append((col,row,node.val))
            if node.left:
                queue.append((node.left,col-1,row+1))
            if node.right:
                queue.append((node.right,col+1,row+1))

        level_list.sort()
        col_dict = defaultdict(list)
        for col,row,value in level_list:
            col_dict[col].append(value)
        result=[]
        for x in col_dict:
            result.append(col_dict[x])

        return result                    


        