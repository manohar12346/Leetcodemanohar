#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        x=[0]*26
        for i in s:
            if ord(i)>=ord('a') and ord(i)<=ord('z') :
                x[ord(i)-ord('a')]+=1
            if ord(i)>=ord('A') and ord(i)<=ord('Z') :
                x[ord(i)-ord('A')]+=1
            
        for i in range(len(x)):
            if x[i]==0:
                
                return 0
        return 1

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
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends