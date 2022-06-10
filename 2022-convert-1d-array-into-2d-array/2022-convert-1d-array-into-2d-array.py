class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        new=[]
        if m*n==len(original):
            
            for i in range(m):
                new.append([0]*n)
            co=0
            for i in range(m):
                for j in range(n):
                    new[i][j]=original[co]
                    co+=1
            return new
        return []