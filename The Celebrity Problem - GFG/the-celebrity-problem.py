#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        i=0
        j=n-1
        while(i<j):
            if M[i][j]==1:
                i=i+1
                j=n-1
                
            else:
                j=j-1
        x=i
        
        for i in range(n):
            if i!=x:
                if M[i][x]!=1:
                    return -1
        return x
        # code here 


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