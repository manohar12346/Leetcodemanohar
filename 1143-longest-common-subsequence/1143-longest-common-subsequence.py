class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def sub(t,h,i,j):
#             if i<0 or j<0:
#                 return 0
            
#             if t[i]==h[j]:
#                 return 1+sub(t,h,i-1,j-1)
#             else:
#                 return max(sub(t,h,i-1,j),sub(t,h,i,j-1))
#         return sub(text1,text2,len(text1)-1,len(text2)-1) Recursive Approach 
                    d=[]
                    for i in range(len(text1)):
                      d.append([0]*len(text2))
                    for i in range(len(text1)):
                        for j in range(len(text2)):
                            if i==0 and j==0:
                                if text1[i]==text2[j]:
                                    d[i][j]=1
                            if i==0:
                                if text1[i]==text2[j]:
                                    d[i][j]=1
                                else:
                                    d[i][j]=d[i][j-1]
                            if j==0:
                                if text1[i]==text2[j]:
                                    d[i][j]=1
                                else:
                                    d[i][j]=d[i-1][j]
                                
                            else:
                                if text1[i]==text2[j]:
                                    d[i][j]=1+d[i-1][j-1]
                                else:
                                    d[i][j]=max(d[i-1][j],d[i][j-1])
                    
                    return d[-1][-1]
                                
                                    
                    
        
          
            