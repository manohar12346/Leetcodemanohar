class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        c=int(len(nums)/3)
        print(dic)
        print(c)
        ans=[]
        for i in dic:
            if dic[i]>c:
                ans.append(i)
        return ans