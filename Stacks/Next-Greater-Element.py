
"""
Next Greater Element


""" 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_ele = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater_ele[prev] = num
            stack.append(num)    

        while stack:
            pop = stack.pop()
            next_greater_ele[pop] = -1

        return [next_greater_ele[num] for num in nums1]        
