class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=sorted(stones)
        
        while(len(stones)>1):
            stones=sorted(stones)
            if len(stones)==2:
                if stones[0]==stones[1]:
                    return 0
            if stones[-1]==stones[-2]:
                del stones[-1]
                del stones[-1]
            else:
                stones[-2]=stones[-1]-stones[-2]
                del stones[-1]
        return stones[0]
            
        