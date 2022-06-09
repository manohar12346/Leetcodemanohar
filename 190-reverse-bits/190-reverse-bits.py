class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        na=bin(n).replace("0b","")
        if len(na)<32:
            d="0"*(32-len(na))
            na=d+na
        
        na=na[::-1]
        
        
    
        return int(na,2)
        