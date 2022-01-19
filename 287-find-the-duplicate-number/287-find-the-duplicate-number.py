class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[0]==nums[nums[0]]:
                return nums[0]
            else:
                a=nums[0]
                nums[0]=nums[nums[0]]
                nums[a]=a            
        