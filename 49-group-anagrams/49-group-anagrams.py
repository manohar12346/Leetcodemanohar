class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in strs:
            k=sorted(i)
            
            if str(sorted(i)) in s:
                s[str(k)].append(i)
               
            else:
                s[str(k)]=[i]
        ans=[]
        print(s)
        for i in s:
            
            ans.append(s[i])
        return ans
        