class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[0]*(max(nums1)+1)
        y=[0]*(max(nums2)+1)
        z=min((max(nums1)+1),(max(nums2)+1))
        for i in nums1:
            x[i]+=1
        for i in nums2:
            y[i]+=1
        ans=[]
        for i in range(z):
            if x[i]>0 and y[i]>0:
                if min(x[i],y[i])>1:
                    for j in range(min(x[i],y[i])):
                        ans.append(i)
                else:
                    ans.append(i)
        return ans
                    
        
        
        
        