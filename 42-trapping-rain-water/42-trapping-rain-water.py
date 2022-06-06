class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0]*len(height)
        ma=height[0]
        for i in range(len(height)):
            left[i]=ma
            
            if ma<height[i]:
                ma=height[i]
        ma=height[i]
        for i in range(len(height)-1,-1,-1):
            right[i]=ma
            
            if ma<height[i]:
                ma=height[i]
        
        ans=0
        for i in range(len(height)):
            if left[i]>height[i] and right[i]>height[i]:
                ans+=min(left[i],right[i])-height[i]
                print(ans,i)
        return ans
        
        