class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        w=[]
        for i in s:
            if i!='-':
                w.append(i.upper())
        c=0
        st=""
        print(w)
        for i in range(len(w)-1,-1,-1):
            c=c+1
            if c==k:
                c=0
                st=st+w[i]
                st=st+'-'
            else:
                st=st+w[i]
        if len(st)==0:
            return ""
                
        if st[-1]=='-':
            c=st[::-1]
            return c[1::]
        else:
            return st[::-1]
        return st
                
                
            
            