class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        x=tickets[k]
        while(x>0):
            for j in range(len(tickets)):
                if tickets[j]==0:
                    continue
                    
                   
                else:
                    ans=ans+1
                    tickets[j]-=1
                    
                if tickets[k]==0:
                    break
            x=x-1
        return ans
        