class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x=[[1]]
        for i in range(1,rowIndex+1):
            x.append([])
            for j in range(0,i+1):
                if j==0 or j==i:
                    x[i].append(1)
                else:
                    x[i].append(x[i-1][j-1]+x[i-1][j])
        return x[-1]
        