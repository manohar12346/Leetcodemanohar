class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p)
        ans=[]
        for i in range(0,(len(s)-len(p)+1)):
            if p==sorted(s[i:i+len(p)]):
                ans.append(i)
        return ans
        