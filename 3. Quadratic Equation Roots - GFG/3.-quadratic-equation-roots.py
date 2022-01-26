#User function Template for python3



class Solution:
	def quadraticRoots(self, a, b, c):
	    d=(b**2 - 4*a*c)
	    if d<0:
	        return [-1]
	    d=d**(1/2)
	    ans=(-b + d)//(2*a)
	    an=(-b - d)//(2*a)
	    ma=max(ans,an)
	    mi=min(ans,an)
	    
	    return [int(ma),int(mi)]
	    
	    
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends