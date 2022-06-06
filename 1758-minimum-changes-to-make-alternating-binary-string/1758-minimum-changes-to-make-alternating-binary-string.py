class Solution:
    def minOperations(self, s: str) -> int:
        a1,a2="",""
        c='1'
        d='0'
        for i in range(len(s)):
            a1+=c
            a2+=d
            c,d=d,c
        ans,an=0,0
        for i in range(len(s)):
            if s[i]!=a1[i]:
                ans+=1
            if s[i]!=a2[i]:
                an+=1
        return min(ans,an)