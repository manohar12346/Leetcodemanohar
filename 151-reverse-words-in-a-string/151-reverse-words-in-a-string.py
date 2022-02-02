class Solution:
    def reverseWords(self, s: str) -> str:
        st=""
        a=0
        ans=[]
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if a==1:
                    ans.append(st)
                a=0
                st=""
            else:
                st=s[i]+st
                a=1
            if i==0:
                if a==1:
                    ans.append(st)
        an=""
        
        for i in range(len(ans)):
            an+=ans[i]+" "
        return an[0:len(an)-1]
                
            
            