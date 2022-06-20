#User function Template for python3

class Solution:
    def assignMiceHoles(self, N , M , H):
        # code here
        M=sorted(M)
        H=sorted(H)
        ma=-100000000
        for i in range(len(M)):
            if abs(M[i]-H[i])>ma:
                ma=abs(M[i]-H[i])
        return ma

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        M=list(map(int,input().split()))
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.assignMiceHoles(N,M,H))
# } Driver Code Ends