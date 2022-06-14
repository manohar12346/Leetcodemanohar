#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        i=0
        j=n-1
        while(i<j):
            if M[i][j]==0:
                j-=1
            else:
                i=i+1
        c=i
        for i in range(n):
            if M[c][i]==1 or M[i][c]==0:
                if i!=c:
                    return -1
            
        return c


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends