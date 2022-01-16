class Solution:
    def longestPalindrome(self, s: str) -> int:
        c={}
        for i in range(len(s)):
            if s[i] in c:
                c[s[i]]+=1
            else:
                c[s[i]]=1
        s=set(s)
        mi=1001000
       
        od=0
        ans=0
        for i in s:
            if c[i]%2==0 :
                ans=ans+c[i]
                if c[i]<mi:
                    mi=c[i]
            elif c[i]%2==1:
                ans=ans+c[i]-1
                od=1
                
        if od==1:
            return ans+1
       
        return ans
        
            
            
            
        
            
        
        
        