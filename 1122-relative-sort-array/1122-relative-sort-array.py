class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x=[0]*(max(arr1)+1)
        for i in arr1:
            x[i]+=1
        a=[]
        for i in arr2:
            
            for j in range(x[i]):
                a.append(i)
            x[i]=0
        print(x)
        for i in range(len(x)):
            if x[i]>0:
                for j in range(x[i]):
                    a.append(i)
        return a
    
        
                
        