class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        s=[]
        p=1
        
        for i in nums:
            product*=i
        if nums.count(0)==1:
            for i in nums:
                if i!=0:
                    p=p*i
            for i in nums:
                if i==0:
                    s.append(p)
                else:
                    
            
                    s.append(product//i)
        else:
            for i in nums:
                if i==0:
                    s.append(0)
                else:
                    
                    s.append(product//i)
            
        return s
        