#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        # code here
        i=0
        j=len(arr)-1
        one=-1
        ze=-1
        while(i<j):
            if arr[i]==1 and one==-1:
                one=i
            if arr[j]==0 and ze==-1:
                ze=j
            if one!=-1 and ze!=-1:
                arr[one],arr[ze]=arr[ze],arr[one]
                one,ze=-1,-1
                
            if one==-1 and ze!=-1:
                i=i+1
            if one!=-1 and ze==-1:
                j=j-1
            if one==-1 and ze==-1:
                i=i+1
                j=j-1
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