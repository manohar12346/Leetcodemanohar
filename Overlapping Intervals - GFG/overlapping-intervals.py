class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals=sorted(Intervals)
		ans=[]
		i=0
		while(i<len(Intervals)):
		    c=Intervals[i][1]
		    j=i+1
		    while(j<len(Intervals) and c>=Intervals[j][0]):
		        
		        c=max(c,Intervals[j][1])
		        j+=1
		    ans.append([Intervals[i][0],c])
		    i=j
	
		return ans
		
            
#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends