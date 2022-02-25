#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    s=[]
    for i in S:
        s.append(i)
    top=len(s)-1
    st=""
    while(top>=0):
        st+=s[top]
        top=top-1
    return st
    
    
    #Add code here

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends