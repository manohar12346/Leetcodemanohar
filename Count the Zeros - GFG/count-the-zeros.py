#User function Template for python3

class Solution:
    def countZeroes(self, arr, n):
        # code here
        i=0
        j=len(arr)-1
        ans=-1
        while(i<j):
            mid=(i+j)//2
            if arr[mid]==0:
                if mid==0:
                    return len(arr)
                if arr[mid-1]==1:
                    return len(arr)-mid
                if arr[mid-1]==0:
                    j=mid-1
            if arr[mid]==1:
                if mid==len(arr)-1:
                    return 0
                if arr[mid+1]==0:
                    return len(arr)-mid-1
                if arr[mid+1]==1:
                    i=mid+1
        return len(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends