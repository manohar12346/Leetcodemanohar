#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        k=0
        a=0
        if len(str1)==len(str2):
            for i in range(len(str1)):
                if str1[i]!=str2[i-2]:
                    k=1 
                    break
            for i in range(len(str1)):
                if str1[i]!=str2[(i+2)%len(str1)]:
                    
                    a=1
                    break
            if a==1 and k==1:
                return 0
            else:
                return 1
        return 0
                    
                
            
                    
            

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
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends