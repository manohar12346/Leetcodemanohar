class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums)==1:
            return nums[0]
        print(nums)
        for i in range(0,len(nums)):
            if i==0:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            if i==len(nums)-1:
                    if nums[i]!=nums[i-1]:
                        return nums[i]
            else:
                if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                    return nums[i]
            