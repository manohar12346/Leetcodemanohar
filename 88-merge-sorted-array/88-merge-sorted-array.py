class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
    
            
        """
        i=0
        while(i!=n):
            j=m-1
            while(j>-1 and nums1[j]>nums2[i]):
                
                nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
                j=j-1
            if j==m:
                print("x")
                return nums1[0:m]+nums2[i::]
            nums1[j+1]=nums2[i]
            print(nums1)
            i=i+1
            m=m+1
        return nums1        
                
            
                
        
            
            
        
        