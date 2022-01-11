class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums=sorted(nums)
        ans=[]
        if len(nums)<=1:
            return []
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while(l<r):
                su=nums[i]+nums[l]+nums[r]
                if su<0:
                    l=l+1
                elif su>0:
                    r=r-1
                else:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
        return ans