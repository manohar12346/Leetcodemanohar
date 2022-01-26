#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        n=N
        if (n < 0):
            return 0
        if (n <= 1):
            return 1
        x = ((n * math.log10(n / math.e) +
              math.log10(2 * math.pi * n) /2.0));
        return math.floor(x) + 1
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends