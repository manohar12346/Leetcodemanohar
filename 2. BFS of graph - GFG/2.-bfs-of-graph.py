#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        ans=[]
        vis=[0]*V
        queue=[0]#insert the elements only visisted in the queue
        vis[0]=1
        while(len(queue)>0):
            ans.append(queue[0])# if there is a elemnt in queue that means it had visited and then added to queue
            for i in adj[queue[0]]:# traverse in adj list and check its childs 
                if vis[i]==0:# if child is not visited make child visited and add to queueu
                    vis[i]=1
                    queue.append(i)
            queue.remove(queue[0])
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