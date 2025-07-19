"""

Largest Rectangle


"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack=[]
        n = len(heights)
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                w = i-j
               
                max_area= max(max_area,h*w)
                start = j
            stack.append((height,start))
        while stack:
            h,j = stack.pop()
            w = n-j
            max_area = max(max_area,h*w)

        return max_area            
       
        