#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        ans=[]
        
        f=0
        s=0
        t=0
        while(f<n1 and s<n2 and t<n3):
            if A[f]>B[s] and A[f]==C[t]:
                s=s+1
            elif A[f]>C[t] and A[f]==B[s]:
                t=t+1
            elif B[s]>A[f] and B[s]==C[t]:
                f=f+1
            elif B[s]>C[t] and B[s]==A[f]:
                t=t+1
            elif B[s]>C[t] and B[s]>A[f]:
                t=t+1
                f=f+1
            elif C[t]>B[s] and C[t]>A[f]:
                f=f+1
                s=s+1
            elif A[f]>C[t] and A[f]>B[s]:
                 t=t+1
                 s=s+1
            else:
                
                if A[f-1]!=A[f] or f==0:
                    ans.append(A[f])
                f=f+1
                t=t+1
                s=s+1
        return ans
                
            
            
        
            
        # your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends