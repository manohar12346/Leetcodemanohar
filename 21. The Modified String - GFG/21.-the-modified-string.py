
#User function Template for python3

class Solution:
    
    #Function to find minimum number of characters which Ishaan must insert  
    #such that string doesn't have three consecutive same characters.
    def modified(self,s):
        #code here
        cnt=0
        c=""
        ans=0
        for i in range(len(s)):
            if cnt==3:
                ans+=1
                cnt=1
            if c==s[i]:
                cnt+=1
            else:
                c=s[i]
                cnt=1
        if cnt==3:
            return ans+1
        return ans
            
            
            

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
        print(obj.modified(s))
# } Driver Code Ends