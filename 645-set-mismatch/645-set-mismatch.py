class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x={}
        x_=-1
        for i in nums:
            if i in x:
                x_=i
            else:
                x[i]='q'
            
        
            
        g=len(nums)
        return [x_,(((g*(g+1))//2))- (sum(nums)-x_)]
                