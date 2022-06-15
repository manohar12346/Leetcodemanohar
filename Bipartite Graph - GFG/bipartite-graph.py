class Solution:
	def isBipartite(self, V, adj):
		#code here]
		visi=[0]*V
		
		colors=[-1]*V
		def bfs(sr):
    		queue=[sr]
    		while(len(queue)):
    		    for i in adj[queue[0]]:
    		       
    		            if colors[i]==-1:
    		                colors[i]=1+colors[queue[0]]
    		                queue.append(i)
    		       
    		            if colors[i]==colors[queue[0]]:
    		                return False
    		    queue.remove(queue[0])
	    for i in range(v):
	        if visi[i]==0:
	            if bfs(i)==False:
	                return False
	            
	    return True
		              

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends