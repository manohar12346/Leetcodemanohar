class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        h=len(nums)-1
        p,po=-1,-1
        while(l<=h):
            mid=(l+h)//2
            
            
            if nums[mid]==target:
                p=mid
            if target<=nums[mid]:
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
                print(po)
            if target>=nums[mid]:
                l=mid+1
                print(mid)
            else:
                
                h=mid-1
            
                
        return [p,po] 
        
       
            
        
                
        