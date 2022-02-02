class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        d=10000000
        for i in strs:
            if len(i)<d:
                d=len(i)
                a=i
        ans=0
        o=0
        for i in range(len(a)):
            c=0
            for j in strs:
                if j[i]==a[i]:
                    c=c+1
                else:
                    o=1
                    break
            if c==len(strs):
                ans=ans+1
            if o==1:
                break
        return a[0:ans]
                    