class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        x=[]
        
        an=""
        def subseq(inp,out=[]):
            if len(inp)==0:
                
                x.append(out)
            else:
                subseq(inp[1:],out+[inp[0]])
                subseq(inp[1:],out)
        subseq(nums)
        return (x)
    