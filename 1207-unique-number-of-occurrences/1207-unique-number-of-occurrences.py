class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x={}
        for i in arr:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        c=-1
        d=set(arr)
        l=[]
        for i in x:
            l.append(x[i])
        l=set(l)
        if len(l)==len(d):
            return True
        
        return False
            
        