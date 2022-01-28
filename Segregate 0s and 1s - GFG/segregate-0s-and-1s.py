#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        # code here
        j=0
        for i in range(len(arr)):
            if arr[i]==0:
                arr[j]=0
                j=j+1
        for i in range(j,len(arr)):
            arr[i]=1
            
        return arr
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends