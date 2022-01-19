class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x={}
        for i in range(len(nums2)):
            x[nums2[i]]=i
        a=[]
        for i in nums1:
            c=x[i]
            ans=-1
            for j in range(c+1,len(nums2)):
                if nums2[j]>i:
                    ans=j
                    a.append(nums2[j])
                    break
            if ans==-1:
                a.append(-1)
        return a
                