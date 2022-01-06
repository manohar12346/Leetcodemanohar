class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x=[]
        ans=[]
        
        for i in range(len(words)):
            x.append([0]*26)
            for j in words[i]:
                x[-1][ord(j)-ord('a')]+=1
        print(x)
        for i in range(26):
            d=0
            mo=100000
            for j  in range(0,len(words)):
                if x[j][i]==0:
                    print(i)
                    d=1
                    break
                else:
                    if mo>x[j][i]:
                        mo=x[j][i]
            if d==0:
                for k in range(mo):
                    ans.append(chr(i+ord('a')))
        return ans
                    
            
                
                