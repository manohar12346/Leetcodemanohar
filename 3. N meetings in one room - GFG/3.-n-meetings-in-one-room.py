#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        x=[]
        for i in range(len(start)):
            x.append([end[i],start[i]])
        x=sorted(x)
        ans=0
        c=x[0][0]
        
        for i in range(1,len(start)):
            if c<x[i][1]:
                ans=ans+1
                
                c=x[i][0]
        return ans+1
                
                
                
        
        
        
            

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
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends