class Solution:
    def minimumMoves(self, s: str) -> int:
        ans=0
        i=0
        while(i<len(s)):
            if s[i]=='X':
                i=i+3
                ans=ans+1
            else:
                i=i+1
           
        return ans
        