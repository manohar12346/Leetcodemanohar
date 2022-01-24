class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while(nums[0]!=nums[nums[0]]):
        
            c=nums[0]
            nums[0]=nums[nums[0]]
            nums[c]=c
        return nums[0]   
        