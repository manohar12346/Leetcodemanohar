class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        ans=0
        an=0
        start=0
        for i in range(len(s)):
            if s[i] in h and start<=h[s[i]]:
                
                    an=i-h[s[i]]
                   
                    start=h[s[i]]+1
                    h[s[i]]=i            
            else:
                an=an+1
                h[s[i]]=i
                
           
            if ans<an:
                ans=an
     
        return ans
                
                
                