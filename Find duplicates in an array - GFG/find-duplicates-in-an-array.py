class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	ans=[]
    	for i in range(n):
    	    arr[arr[i]%n]+=n
    	for i in range(n):
    	    if arr[i]//n>1:
    	        ans.append(i)
    	if len(ans):
    	    return ans
    	else:
    	    return [-1]
    	   
    	    
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends