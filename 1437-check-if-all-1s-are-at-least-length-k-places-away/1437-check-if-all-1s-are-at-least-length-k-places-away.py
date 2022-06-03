class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=-1
        for i in range(len(nums)):
            if nums[i]==1 and c==-1:
                c=i
            elif nums[i]==1:
                if abs(c-i)<=k:
                    
                    return False
                c=i
                
        return True
        