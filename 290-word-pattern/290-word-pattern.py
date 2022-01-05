class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x=[-1]*26
        s=s.split(" ")
        o={}
        if len(s)!=len(pattern):
            return False
        else:
            
       
            for i in range(len(pattern)):
                if x[ord(pattern[i])-ord('a')]!=-1:
                    if s[i]!=x[ord(pattern[i])-ord('a')]:

                        return False
                else:
                    if s[i] in o:
                        return False
                    x[ord(pattern[i])-ord('a')]=s[i]
                    o[s[i]]=1

            return True
                
        