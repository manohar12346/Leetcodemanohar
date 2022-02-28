
#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        x=[]
        y=[]
        for i in s:
            if i.isupper():
                y.append(i)
            else:
                x.append(i)
        x=sorted(x)
        y=sorted(y)
        x_=0
        y_=0
        su=""
        for i in range(len(s)):
            if s[i].isupper():
                su=su+y[y_]
                y_+=1
            else:
                su=su+x[x_]
                x_+=1
        return su

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends