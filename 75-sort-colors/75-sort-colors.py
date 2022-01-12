class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=[0]*3
        for i in nums:
            x[i]+=1
        ans=[]
        for i in range(len(x)):
            for j in range(x[i]):
                ans.append(i)
        print(ans)
        for i in range(len(nums)):
            nums[i]=ans[i]
        return ans
        