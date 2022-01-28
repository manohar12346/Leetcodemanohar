class Solution:
    def numSplits(self, s: str) -> int:
        x=[0]*len(s)
        y=[0]*len(s)
        firs={}
        secon={}
        for i in range(len(s)):
            if s[i] not in firs:
                firs[s[i]]=10
                if i==0:
                    x[i]=1
                else:
                    x[i]+=x[i-1]+1
            else:
                x[i]=x[i-1]
        for j in range(len(s)-1,-1,-1):
            if s[j] not in secon:
                if j==len(s)-1:
                    y[j]=1
                    secon[s[j]]=10
                else:
                    
                    y[j]+=y[j+1]+1
                    secon[s[j]]=10
            else:
                y[j]=y[j+1]
        print(x,y)
        
        ans=0
        for i in range(len(x)-1):
            if x[i]==y[i+1]:
                ans=ans+1
        return ans
                
                
        