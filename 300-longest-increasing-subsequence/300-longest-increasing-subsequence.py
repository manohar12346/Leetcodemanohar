class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        x=[1]* len(nums)
        arr=nums
        l=0
        for i in range(len(nums)):
            for j in range(0,i):
                if arr[i]>arr[j]:
                    if x[i]<=x[j]:
                        x[i]=x[j]+1
        return max(x)
                    