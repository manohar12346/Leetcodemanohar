class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        s=sorted(intervals)
        l=s[0][0]
        h=s[0][1]
        ans=[]
        for i in range(1,len(s)):
            if h<s[i][0]:
                ans.append([l,h])
                l=s[i][0]
                h=s[i][1]
                    
            else:
                if h<s[i][1]:
                    h=s[i][1]
        ans.append([l,h])
        return ans
                
            