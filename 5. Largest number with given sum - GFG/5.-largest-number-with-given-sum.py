#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        ans=""
        if 9*n<s:
            return -1
        for i in range(n):
            if s>=9:
                s=s-9
                ans+='9'
            else:
                ans+=str(s)
                s=0
        return int(ans)
                
            
        
        
        # code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends