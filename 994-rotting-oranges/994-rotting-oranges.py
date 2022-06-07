class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        f=0
        ap=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    ap.append([i,j,0])
                    
                elif grid[i][j]==1:
                    f+=1
        if f==0:
            return 0
        else:
            check=[0]
            ans=1
            while(len(ap)):
                yes=0
                l,r,c=ap[0][0],ap[0][1],ap[0][2]
                if l-1>-1:
                    
                    if grid[l-1][r]==1:
                        yes=1
                        grid[l-1][r]=2
                        if [l-1,r] not in ap:
                            ap.append([l-1,r,c+1])
                        
                if l+1<len(grid):
                    
                   
                        if grid[l+1][r]==1:
                            yes=1
                            grid[l+1][r]=2
                            if [l+1,r] not in ap:
                                ap.append([l+1,r,c+1])
                           
                if r-1 >-1:  
                    if grid[l][r-1]==1:
                        yes=1
                        grid[l][r-1]=2
                        if [l,r-1] not in ap:
                            ap.append([l,r-1,c+1])
                        
                if r+1<len(grid[0]):
                    if grid[l][r+1]==1:
                        yes=1
                        grid[l][r+1]=2
                        if [l,r+1] not in ap:
                            ap.append([l,r+1,c+1])
                        print([l,r+1])
                if yes==1:
                    if c not in check:
                        ans+=1
                        check.append(c)
                    
                ap.remove(ap[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return ans
                        
                    
                    
                    
            
                  
                  
            
            
                    