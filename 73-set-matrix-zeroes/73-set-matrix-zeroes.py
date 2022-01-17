class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x=[0]*(max(len(matrix[0]),len(matrix)))
        y=[0]*(max(len(matrix[0]),len(matrix)))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x[i]=1
                    y[j]=1
        print(x)
        print(y)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if x[i]==1 or y[j]==1:
                    matrix[i][j]=0
        print(matrix)
        
        return matrix