class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c=1
        ans=0
        if len(nums)==1:
            return True
            
        for i in range(len(nums)-2,-1,-1):
            print(nums[i],c)
            if nums[i]>=c:
                c=1
                ans=1
                print(nums[i])
                
            else:
                c=c+1
                ans=0
        if ans==1:
            return True
        else:
            return False
        
        
                
                    
        