class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # def s(w,e,i,j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if w[i]==e[j]:
        #         return s(w,e,i-1,j-1)
        #     else:
        #         return 1+min(min(s(w,e,i,j-1),s(w,e,i-1,j-1)),s(w,e,i-1,j))
        # return s(word1,word2,len(word1)-1,len(word2)-1)
    
        x=[]
        for i in range(len(word1)+1):
            x.append([0]*(len(word2)+1))
        for i in range(len(word2)+1):
            x[0][i]=i
        for j in range(len(word1)+1):
            x[j][0]=j
            
        for i in range(1,len(x)):
            for j in range(1,len(x[0])):
                if word1[i-1]==word2[j-1]:
                    x[i][j]=x[i-1][j-1]
                else:
                    x[i][j]=1+min(min(x[i][j-1],x[i-1][j-1]),x[i-1][j])
        
        return x[-1][-1]              
    
        