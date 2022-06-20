class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx,mn=1,1
        res=max(nums)
        for num in nums:
            temp=mx*num

            mx=max(mx*num,mn*num,num)
            mn=min(temp,mn*num,num)
            res=max(res,mx)
        return res