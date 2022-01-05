class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trus=[0]*(n+1)
        r=[0]*(n+1)
        for i in trust:
            trus[i[1]]+=1
            r[i[0]]+=1
        for i in range(1,len(trus)):
            if trus[i]==n-1:
                if r[i]==0:
                    return i
        return -1
        
            