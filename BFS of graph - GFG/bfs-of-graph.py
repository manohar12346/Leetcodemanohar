#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visi=[0]*len(adj)
        visi[0]=1
        x=[0]
        ans=[]
        while(len(x)>0):
            ans.append(x[0])
            for i in adj[x[0]]:
                if visi[i]==0:
                    visi[i]=1
                    x.append(i)
            x.remove(x[0])
        return ans
                    
            
            

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends