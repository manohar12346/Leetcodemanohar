class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums=sorted(nums)
        ans=[]
        
        if len(nums)<=1:
            return []
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            while(l<h):
                s=nums[l]+nums[h]+nums[i]
                if s<0:
                    l=l+1
                if s>0:
                    h=h-1
                if s==0:
                    if [nums[i],nums[l],nums[h]] not in ans:
                        ans.append([nums[i],nums[l],nums[h]])
                    l=l+1
                    h=h-1
        
        return ans
                
                    