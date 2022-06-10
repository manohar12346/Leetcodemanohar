class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        co=0
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                co+=1
            if co==3:
                return nums[i]
        if len(nums)>1:
            if nums[-1]!=nums[-2]:
                if co+1==3:
                    return nums[-1]
            if nums[-1]==nums[-2]:
                if co+1==3:
                    return nums[-2]
        return max(nums)
                
        