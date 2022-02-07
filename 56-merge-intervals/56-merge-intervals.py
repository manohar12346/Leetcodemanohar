class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        inte=sorted(intervals)
        l,h=inte[0][0],inte[0][1]
        ans=[]
        
        
        for i in range(1,len(inte)):
            if h>=inte[i][0]:
                if h>inte[i][1]:
                    h=h
                else:
                    h=inte[i][1]
            
            else:
                
                
                ans.append([l,h])
                l=inte[i][0]
                h=inte[i][1]
                
       
        ans.append([l,h])
        return ans
                