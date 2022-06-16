class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        visi=[0]*len(adj)
        dis=[1000000]*len(adj)
        visi[S]=1
        for i in adj[S]:
            dis[i[0]]=i[1]
        dis[S]=0
        
        def find_node():
            ind=-1
            mi=100000000
            for i in range(len(dis)):
                if visi[i]==0:
                    if dis[i]<mi:
                        
                        mi=dis[i]
                        ind=i
            visi[ind]=1
            return ind
        
        
        
        for i in range(len(adj)):
            node=find_node()
            
            for i in adj[node]:
                if dis[i[0]]>dis[node]+i[1]:
                    dis[i[0]]=dis[node]+i[1]
            
        return dis
                
            
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends