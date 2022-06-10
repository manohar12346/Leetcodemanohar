class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f=-100000000000000000000000
        s=-1000000000000000000000000
        t=-1000000000000000000000000
        f=max(nums)
        
        for i in nums:
            if i<f and i>s:
                s=i
        for i in nums:
            if i<s and i>t:
                t=i
        print(t)
        if t!=-1000000000000000000000000:
            return t
        return f
                
        