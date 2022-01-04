class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        h=len(nums)-1
        p,po=-1,-1
        while(l<=h):
            mid=(l+h)//2
            
            
            if nums[mid]==target:
                p=mid
                h=mid-1# here once we find the element try to check its left to find whetehr the same element is there in its left such we can get the element in the left most side
            elif target<nums[mid]:
                h=mid-1
            elif target>nums[mid]:
                l=mid+1
        l=0
        h=len(nums)-1
        print(l,h)
        while(l<=h):
            mid=(l+h)//2
            print(l,h)
            
            
            if nums[mid]==target:
                po=mid
                l=mid+1# here once we find the element try to check its right to find whetehr the same element is there in its right such we can get the element in the right most side
            elif target>nums[mid]:
                l=mid+1
                
            else:
                
                h=mid-1
            
                
        return [p,po] 
        
       
            
        
                
        