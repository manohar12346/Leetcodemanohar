class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=-100000000000000000000000000
        blank=-1
        co=0
        for i in range(len(nums)):
            if nums[i]!=prev:
                prev=nums[i]
                if blank>0 and blank<i:
                    nums[i],nums[blank]=nums[blank],nums[i]
                    
                    if nums[blank+1]=="_":
                        blank+=1
                    else:
                        blank=-1
            else:
                nums[i]="_"
                if blank<0:
                    blank=i
                co+=1
           
           
        return len(nums)-co