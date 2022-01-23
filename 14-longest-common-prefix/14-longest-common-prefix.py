class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        d=10000000
        for i in strs:
            if len(i)<d:
                d=len(i)
                a=i
        ans=100000
        for i in range(len(strs)):
            co=0
            for j in range(0,d):
                if strs[i][j]==a[j]:
                    co=co+1
                else:
                    break
            if co<ans:
                ans=co
                print(ans)
        return a[0:ans]
                