class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[nums2[-1]]
        ans=[0]*len(nums2)
        ans[-1]=-1
        dic={}
        for i in range(len(nums2)):
            dic[nums2[i]]=i
        for i in range(len(nums2)-2,-1,-1):
            if nums2[i]<s[-1]:
                ans[i]=s[-1]
            else:
                
                while(len(s)>0 and nums2[i]>s[-1]):
                    s.pop()
               
                if len(s)==0:
                    
                    ans[i]=-1
                    
                else:
                    ans[i]=s[-1]
            s.append(nums2[i])
       
        an=[]
        for i in nums1:
            an.append(ans[dic[i]])
        return an
            
        print(ans)
            
            
        