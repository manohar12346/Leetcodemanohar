class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split(" ")
        dic={}
        f={}
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] not in f:
                    dic[pattern[i]]=s[i]
                    f[s[i]]=1
                else:
                    return False
            else:
                if dic[pattern[i]]!=s[i]:
                    return False
        return True