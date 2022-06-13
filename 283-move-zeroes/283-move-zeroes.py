class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while(i<len(nums) and j<len(nums)):
            if nums[i]==0:
                while(j<len(nums) and nums[j]==0):
                    j+=1
                if j<len(nums):
                    nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1 
                j+=1
        return nums