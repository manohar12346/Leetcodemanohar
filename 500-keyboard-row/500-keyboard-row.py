class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        x="qwertyuiopQWERTYUIOP"
        y="asdfghjklASDFGHJKL"
        z="zxcvbnmZXCVBNM"
        q=[]
        for i in words:
            c=0
            if i[0] in x : 
                for j in i:
                    if j in x:
                        c=c+1
                if c==len(i):
                    q.append(i)
            elif i[0] in y : 
                for j in i:
                    if j in y:
                        c=c+1
                if c==len(i):
                    q.append(i)
            else:
                
                for j in i:
                    if j in z:
                        c=c+1
                if c==len(i):
                    q.append(i)
        return q