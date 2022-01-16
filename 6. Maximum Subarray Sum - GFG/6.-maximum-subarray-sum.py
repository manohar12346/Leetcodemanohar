#User function Template for python3

def maxSubArraySum(array):
	'''
	Returns the maximum subarray sum.
	
	array (list): A list of numbers.
	'''
	# Complete this function
	su=0
	ans=0
	if max(array)<0:
	    return max(array)
	for i in array:
	    su=su+i
	    if su<0:
	        su=0
	    if ans<su:
	        ans=su
    return ans
	   
	        


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		array = [int(x) for x in input().strip().split()]
		print(maxSubArraySum(array))
# } Driver Code Ends