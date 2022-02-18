#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        # 1.REV 0 to d
        #2.REV d+1 to n
        #3. REV 0 to n
        l=0
        h=D-1
        while(l<h):
            A[l],A[h]=A[h],A[l]
            l=l+1
            h=h-1
        l=D
        h=N-1
        while(l<h):
            A[l],A[h]=A[h],A[l]
            l=l+1
            h=h-1
        l=0
        h=N-1
        while(l<h):
                A[l],A[h]=A[h],A[l]
                l=l+1
                h=h-1
        return A
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends