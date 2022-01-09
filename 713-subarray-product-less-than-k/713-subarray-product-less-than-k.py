class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        p=1
        c=0
        an=0
        if k==0:
            return 0
        while(i<len(nums) ):
            p=p*nums[i]
            if p>=k:
                
                
                while(p>=k and c<len(nums)):
                    p=p//nums[c]
                    c=c+1
                if c==len(nums):
                    return an
                else:
                    an+=i-c+1
                    i=i+1

            else:
                an+=i-c+1
                i=i+1
                
            
        
        return an
        