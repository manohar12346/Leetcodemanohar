#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        sum=0.0
        j=1
        while(j<=N):
            #sum stores log(j) + log(j+1) + ... + log(N) 
            sum+=(math.log10(j))
            j+=1
            
        return 1+ math.floor(sum)
        
        
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