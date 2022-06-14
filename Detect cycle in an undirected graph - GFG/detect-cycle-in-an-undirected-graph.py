class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		v=V
		visi=[0]*v
		ans=[]
		def cy(V,adj,pare):
		    visi[V]=1
		    for i in adj[V]:
		        if visi[i]==0:
		            
		            if cy(i,adj,V):
		                return True
		       
		        elif i!=pare:
		                return True
		    return False
		
		for i in range(v):
		    if visi[i]==0:
		        if cy(i,adj,-1):
		            return True
	    return False
		    
		    

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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends