class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        s=[0]*(max(len(nums),max(nums))+1)
        for i in nums:
            s[i]+=1
        che=[]
        d=max(s)
        for i in range(len(s)):
            if s[i]==d:
                che.append(i)
        inde=[0]*(max(che)+1)
        for i in range(len(inde)):
            inde[i]=[]
        for i in range(len(nums)):
            if nums[i] in che:
                inde[nums[i]].append(i)
        print(inde)
        ans=[]
        for i in inde:
            ma=10000000
            if i!=[]:
                for j in range(len(i)-d+1):
                    diff=abs(i[j]-i[j+d-1])+1
                    if diff<ma:
                        ma=diff
            ans.append(ma)
        return min(ans)
                    
    
        
        