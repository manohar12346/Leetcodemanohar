class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        for i in range(len(s)):
            if s[i]=="#":
                j=i-1
                while(j>=0):
                    if s[j]!='#' and s[j]!="":
                        
                        s[j]=""
                        break
                    j=j-1
        for i in range(len(t)):
            if t[i]=="#":
                j=i-1
                while(j>=0):
                    if t[j]!='#' and t[j]!="":
                        
                        t[j]=""
                        break
                    j=j-1
        print(s,t)
        a,b="",""
        
        for i in range(len(s)):
            if s[i]!='#' and s[i]!="":
                a=a+s[i]
        for i in range(len(t)):
            if t[i]!='#' and t[i]!="":
                b=b+t[i]
        print(a,b)
        if a==b:
            return True
        return False
                        
            
                    
        