#User function Template for python3


#Function to check if the pattern is present in string or not.
def Rabin_Karp(pat, txt, q):
    #code here
    su=0
    j=0
    q=0
    for i in pat:
        q+=ord(i)
    
    for i in range(len(txt)):
        if i<len(pat):
            su+=ord(txt[i])
        else:
            if su==q:
                
                if txt[i-len(pat):i]==pat:
                    return True
               
            
            su=su-ord(txt[j])
            j=j+1
            su+=ord(txt[i])
    
    if su==q:
        
        if txt[len(txt)-len(pat):len(txt)]==pat:
                    return True
    return False
        

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
        txt=str(input())
        pat=str(input())
        q=101
        if(Rabin_Karp(pat,txt,q)):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends