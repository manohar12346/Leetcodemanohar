class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        ans=10000000000
        a=10000
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            
            while(l<h):
                
                s=nums[l]+nums[h]+nums[i]
                
                if ans>abs(target-s):
                    ans=abs(target-s)
                   
                    
                    a=s
                if s>target:
                    h=h-1
                if s<target:
                    l=l+1
                if s==target:
                    
                    return target
        return a
                
                
            
                
                
        