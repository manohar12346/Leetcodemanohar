import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        d=(len(b)//len(a))+1
        k=a
        
        if b in a:
            return 1
        for i in range(d):
            a=a+k
            if b in a:
                return i+2
        return -1
            
            
            