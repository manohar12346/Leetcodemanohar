class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        a=[0]*(N+1)
        for i in range(N):
            if arr[i]<=N:
                a[arr[i]]+=1
        
        for i in range(0,len(a)-1):
            arr[i]=a[i+1]
            
        return arr
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends