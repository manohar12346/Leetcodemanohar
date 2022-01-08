class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        c=0
        o=0
        i=0
        
        while(c!=1):
            i=i+1
            o=i
            
            for p in range(len(nums)):
                o=o+nums[p]
                if o<1:
                    c=0
                    break
                c=1
           
        return i
                    
                
            