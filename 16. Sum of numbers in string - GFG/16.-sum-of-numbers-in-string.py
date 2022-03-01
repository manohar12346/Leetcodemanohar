
#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        su=0
        i=0
        while(i<len(s)):
            if s[i].isdigit():
                j=i
                st=""
                while(j<len(s) and (s[j].isdigit())):
                    
                    st+=s[j]
                    j+=1
                su+=int(st)
                i=j
            i=i+1
        return su
                    
                    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        print(obj.findSum(s))
# } Driver Code Ends