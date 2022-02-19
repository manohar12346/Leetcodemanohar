#User function Template for python3

class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        ans=0
        s=1
        for i in range(n-1):
            if (arr[i]%2==0 and arr[i+1]%2==1) or (arr[i+1]%2==0 and arr[i]%2==1):
                s=s+1
            else:
                s=1
            ans=max(ans,s)
        return ans
                
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maxEvenOdd(arr,n))
# } Driver Code Ends