#User function Template for python3

class Solution:
    
	def nthPoint(self,n):
	   # x=[0]
	   # def j(n):
    # 	    if n==0:
    # 	        x[0]+=1
    # 	        return 
    # 	    if n<0:
    # 	        return 
    	    
    #     	j(n-1)
    #     	j(n-2)
    # 	j(n)
    # 	return x[0]
    	   
		# conversion to other form observe keenly
# 		def j(n):
	        
#     	    if n==0:
    	        
#     	        return 1
#     	    if n<0:
#     	        return 0
    	    
#         	return j(n-1)+j(n-2)
#     	return j(n)
# dynamic programming
            x=[1,1]
            for i in range(2,n+1):
                x.append(x[i-1]+x[i-2])
            
            return x[-1]%(10**9+7)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends