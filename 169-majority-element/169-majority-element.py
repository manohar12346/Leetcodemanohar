class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        c=int(len(nums)/2)
        print(dic)
        print(c)
        for i in dic:
            if dic[i]>c:
                return i