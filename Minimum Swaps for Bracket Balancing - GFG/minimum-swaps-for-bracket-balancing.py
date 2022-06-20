#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        l=0
        c=0
        r=0
        ans=0
        bal=0
        for i in range(len(S)):
            if S[i]=='[':
                
                l+=1
                if bal>0:
                    ans+=bal
                    bal-=1
            if S[i]==']':
                r+=1
                bal=r-l
                
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends