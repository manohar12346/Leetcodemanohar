class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        ie=intervals
        f=ie[0][0]
        g=ie[0][1]
        i=1
        ans=0
        while(i<len(ie)):
            if g>ie[i][0]:
                ans=ans+1
                g=min(g,ie[i][1])
                print(ie[i])
                i=i+1
            else:
                g=ie[i][1]
                i=i+1
        return ans
                
        