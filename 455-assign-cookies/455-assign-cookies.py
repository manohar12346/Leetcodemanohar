class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        g_=0
        s_=0
        ans=0
        while(s_<len(s) and g_<len(g)):
            if g[g_]<=s[s_]:
                ans+=1
                g_+=1
                s_+=1
            else:
                s_+=1
        return ans
        
        