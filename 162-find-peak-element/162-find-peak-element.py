class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        
        
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        while(l<=h):
            mid=(l+h)//2
            
            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            if nums[mid]<nums[mid-1]:
                h=mid-1
            elif nums[mid]<nums[mid+1]:
                l=mid+1
                
            
        
        
        return 0        
                
        
        