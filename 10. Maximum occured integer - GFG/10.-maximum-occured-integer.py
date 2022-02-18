#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,L,R,N,maxx):
        x=[0]*(maxx+2)
        for i in range(N):
            x[L[i]]+=1
            x[R[i]+1]-=1
        m=x[0]
        ans=0
       
        for i in range(len(x)-1):
            
            x[i+1]+=x[i]
            if m<x[i]:
                m=x[i]
                ans=i
        return ans
        
        ##Your code here
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math

A=[0]*1000000


            

def main():
    
    T=int(input())
    
    while(T>0):
        
        global A
        A=[0]*1000000
        
        N=int(input())
        
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        
        maxx=max(R)
        ob=Solution()
        print(ob.maxOccured(L,R,N,maxx))
            
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends