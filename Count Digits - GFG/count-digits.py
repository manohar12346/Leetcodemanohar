#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        c=0
        k=N
        while(N>0):
            
            a=N%10
            if a!=0:
                if k%a==0:
                    c=c+1
                
            N=N//10
        return c
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends