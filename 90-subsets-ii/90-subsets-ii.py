class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def sub(ar,new=[]):
            if len(ar)==0:
                if sorted(new) not in a:
                    a.append(sorted(new))
            else:
                sub(ar[1::],new+[ar[0]])
                sub(ar[1::],new)
        sub(nums)
        return a
        