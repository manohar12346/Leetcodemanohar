#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
	    x=sum(arr)
	    su=0
	    for i in range(len(arr)):
	        
	        
	        if su==x-su-arr[i]:
	            return "YES"
	        su=su+arr[i]
	        
	            
	    return "NO"
    	# code here
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends