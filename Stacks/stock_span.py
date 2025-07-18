"""

stock span



"""



class Solution:
    def calculateSpan(self, arr):
        
        span = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            if not stack:
                span[i] = i+1
            else:
                span[i] = i-stack[-1]
            stack.append(i)
        return span  