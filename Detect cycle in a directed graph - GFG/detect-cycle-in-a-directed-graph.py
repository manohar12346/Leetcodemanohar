#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited=[0]*V
        stack_parent=[0]*V
        def dfs(v):
            visited[v]=1
            stack_parent[v]=1
            for i in adj[v]:
                if visited[i]==0:
                    if dfs(i)==True:
                        return True
                elif stack_parent[i]:
                    return True
            stack_parent[v]=0
            return False
        for i in range(V):
            if visited[i]==0:
               if  dfs(i)==True:
                   return True
        return False
            
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends