#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    x=[]
	    def subset(arr,an,su):
	        if len(arr)==0:
	            x.append(su)
	        else:
	            
	            subset(arr[1:],an,su)
	            subset(arr[1:],an+[arr[0]],su+arr[0])
	    subset(arr,[],0)
	    return sorted(x)
	    
	   
	    
	        
	    
	            
	            
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