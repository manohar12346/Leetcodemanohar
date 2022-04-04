class Solution:
    def longestPalindrome(self, s: str) -> int:
        c={}
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        k=0
        ans=0
        for i in c:
            if c[i]%2==0:
                ans+=c[i]
            else:
                if k==0:
                    k=1
                    ans+=1
                ans+=c[i]-1
        return ans
                
            
        
            
        
        
        