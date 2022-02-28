
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        
        st=list(map(str,S.split(".")))
        s=""
        for i in range(len(st)-1,-1,-1):
            if i==0:
             s=s+st[i]
            else:
                s=s+st[i]+'.'
            
        return s

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends