#User function Template for python3

class Solution:
    #Complete this function
    #Function to find minimum adjacent difference in a circular array.
    def minAdjDiff(self,arr, n):
        ##Your code here
        d=10000000
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])<d:
                d=abs(arr[i]-arr[i+1])
        if d>abs(arr[n-1]-arr[0]):
            d=abs(arr[n-1]-arr[0])
        return d
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3




def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
       
        ob=Solution()
        print(ob.minAdjDiff(arr,n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends