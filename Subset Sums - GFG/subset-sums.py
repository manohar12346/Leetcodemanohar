#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ans=[]
	    def sub(arr,new=[]):
	        if len(arr)==0:
	            ans.append(sum(new))
	        else:
	        
    	        sub(arr[1::],new+[arr[0]])
    	        sub(arr[1::],new)
	    sub(arr)
	    
	    
	        
	    return ans
	            
	            
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends