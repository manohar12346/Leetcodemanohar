class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        x=[0]*(max(len(nums),max(nums))+1)
        ma=0
        for i in nums:
            if i>=0:
                x[i]+=1
            else:
                ma=max(ma,abs(i))
        n=[0]*max(len(nums)+1,ma+1)
        for i in nums:
            if i<0:
                n[abs(i)]+=1
        ans=[]
        
        for i in range(len(x)-1,-1,-1):
            if x[i]>0:
                if k-x[i]>0:
                    k-=x[i]
                    for j in range(x[i]):
                        ans.append(i)
                elif k-x[i]==0:
                    for j in range(x[i]):
                        ans.append(i)
                    k=0
                    break
                else:
                    for j in range(k):
                        ans.append(i)
                    k=0
                    break
                    
                    
        if k>0:
            for i in range(len(n)):
                if n[i]>0:
                    if k-n[i]>0:
                   
                        k-=n[i]
                        for j in range(n[i]):
                            ans.append(-i)
                    elif k==0:
                        for j in range(n[i]):
                            ans.append(-i)
                        
                        break
                    else:
                        for j in range(k):
                            ans.append(-i)
                        break
        d={}
        for i in ans:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        an=[]
        for i in nums:
            if i in d:
                if d[i]>0:
                    an.append(i)
                    d[i]-=1
        
        
        
        
        return an
                    
                    