class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            
            x={}
            for i in nums2:
                if i in x:
                    x[i]+=1
                else:
                    x[i]=1
            ans=[]
            for i in range(len(nums1)):
                if nums1[i] in x:
                    if x[nums1[i]]>0:
                        ans.append(nums1[i])
                        x[nums1[i]]-=1
            
                
                    
                
        else:
            x={}
            for i in nums1:
                if i in x:
                    x[i]+=1
                else:
                    x[i]=1
            ans=[]
            for i in range(len(nums2)):
                if nums2[i] in x:
                    if x[nums2[i]]>0:
                        ans.append(nums2[i])
                        x[nums2[i]]-=1
        return ans           
            
      
        
        
        
        