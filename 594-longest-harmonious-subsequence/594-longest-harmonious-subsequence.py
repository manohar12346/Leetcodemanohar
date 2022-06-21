class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        ma=0
        for i in nums:
            if i  in c and i+1 in c:
                if c[i]>0 and c[i+1]>0:
                    ma=max(ma,c[i]+c[i+1])
        return ma