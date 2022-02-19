#User function Template for python3

class Solution:
    ##Complete this function
    #Function to check if array is sorted and rotated.
    def checkRotatedAndSorted(self,arr,n):
        #code here 
        c=-1
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                c=i+1
                break
        
        if c!=-1:
        # this code is for making rotation to anticlock wise same problem done in some above question
            i=0
            d=c-1
            while(i<d):
                arr[i],arr[d]=arr[d],arr[i]
                i=i+1
                d=d-1
            d=c
            j=n-1
            while(d<j):
                arr[j],arr[d]=arr[d],arr[j]
                j=j-1
                d=d+1
            i=0
            j=n-1
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
                j=j-1
            for i in range(n-1):
                if arr[i]>arr[i+1]:
                    return False
            return True
        return False
                

#{ 
#  Driver Code Starts
import atexit

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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        if ob.checkRotatedAndSorted(a,n) or ob.checkRotatedAndSorted(a[::-1],n):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends