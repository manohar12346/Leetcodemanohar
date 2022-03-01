#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to check if a string is subsequence of other string.
    def isSubSequence(self, A, B):
        j=0
        for i in B:
            if A[j]==i:
                j=j+1
            if j==len(A):
                return True
        return False
        #code here

#{ 
#Driver Code Starts.

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if (ob.isSubSequence(A,B)):
            print("True")
        else:
            print("False")
#} Driver Code Ends