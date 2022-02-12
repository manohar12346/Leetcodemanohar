class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j])) <int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        st=""
        for i in nums:
            st=st+str(i)
        if st[0]=='0':
            return '0'
        return st
        