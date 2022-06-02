class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        li=1
        end=len(s)
        for i in range(1,len(s)):
            l=i-1
            h=i+1
            while(l>=0 and h<len(s) and s[l]==s[h]):
                if li<h-l+1:
                    li=h-l+1
                    start=l
                    
                l=l-1
                h=h+1
            l=i-1
            h=i
            while(l>=0 and h<len(s) and s[l]==s[h]):
                if li<h-l+1:
                    li=h-l+1
                    start=l
                    
                l=l-1
                h=h+1
        if start!=-1:
            return s[start:start+li]
                