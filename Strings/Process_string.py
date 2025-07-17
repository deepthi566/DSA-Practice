"""
Process string with special operations 



"""


class Solution:
    def processStr(self, s: str) -> str:
        

        res=[]
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                res.append(s[i])
            elif s[i] == '*':
                if res:
                    res.pop()
            elif s[i] == '#':
                res.extend(res[:])
                
            elif s[i] == '%':
                res.reverse()
                
        return ''.join(res)        
        