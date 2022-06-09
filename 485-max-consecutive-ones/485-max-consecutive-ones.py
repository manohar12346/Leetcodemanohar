class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        f=0
        b=0
        ans=0
        while(i<=j):
            if nums[i]==1:
                f+=1
            
            if nums[i]==0:
                f=0
            if nums[j]==1:
                b+=1
            if nums[j]==0:
                b=0
            if f>ans:
                ans=f
            if b>ans:
                ans=b
            i+=1
            j=j-1
        
        
            
        if f!=0 and b!=0 :
            if len(nums)%2==0:
                if b+f>ans:
            
                    return b+f
                else:
                    return ans
            else:
                if b+f-1>ans:
                    return b+f
                else:
                    return ans
           
        return ans