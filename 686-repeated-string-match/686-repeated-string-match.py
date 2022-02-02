import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c=math.ceil(len(b)/len(a))
        st=""
        for i in range(c):
            st+=a
        if b in st:
            return c
        else:
            st+=a
            if b in st:
                return c+1
        return -1
        
        