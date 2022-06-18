class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        
        ans=[0]
        def mer(arr):
            if len(arr)>1:
                
                mid=len(arr)//2
                l=arr[0:mid]
                r=arr[mid::]
                mer(l)
                mer(r)
                d=0
                g=0
                k=0
                while(d<len(l) and g<len(r)):
                    if l[d]<=r[g]:
                        arr[k]=(l[d])
                        d+=1
                        k+=1
                    else:
                        arr[k]=(r[g])
                        ans[0]+=len(l)-d
                        g+=1
                        k+=1
                if d<len(l):
                    for i in range(d,len(l)):
                        arr[k]=(l[i])
                        k+=1
                        
                if g<len(r):
                     for i in range(g,len(r)):
                        arr[k]=(r[i])
                        k+=1
        mer(arr)
        
            
        return ans[0]
                    
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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends