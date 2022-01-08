class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in range(0,len(nums)):
            
            s=s+nums[i]
            if s <1:
                c=c+(1-s)
                s=s+(1-s)
            
            print(s,c)        
        if c==0:
            return 1
        return c
                
       
                    
                
            