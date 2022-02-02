class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x=[]
        a=0
        ans=0
        ch_atleast_one_orage=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    x.append([i,j])
                    a=1
                if grid[i][j]==1:
                    ch_atleast_one_orage+=1
                    
        if a==0:
            if ch_atleast_one_orage>0:
                return -1
            else:
                return 0
        
        else:
            while(len(x)!=0):
                d=0
                y=[]
                while(len(x)!=0):
                        i,j=x[0][0],x[0][1]
                        if j+1<len(grid[0]):
                            if grid[i][j+1]==1:
                                if [i,j+1] not in x:
                                    y.append([i,j+1])
                                    d=1
                                    grid[i][j+1]=2

                        if i+1<len(grid):
                            if grid[i+1][j]==1:
                                if [i+1,j] not in x:
                                    y.append([i+1,j])
                                    d=1
                                    grid[i+1][j]=2


                        if i-1>=0:
                            if grid[i-1][j]==1:
                                if [i-1,j] not in x:
                                    y.append([i-1,j])
                                    d=1
                                    grid[i-1][j]=2


                        if j-1>=0:
                             if grid[i][j-1]==1:
                                if [i,j-1] not in x:
                                    y.append([i,j-1])
                                    d=1
                                    grid[i][j-1]=2
                        x.remove(x[0])
                if d==1:
                    ans+=1
                        
                for i in y:
                        x.append(i)
                        
                print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return ans
                  
                  
                  
            
            
                    