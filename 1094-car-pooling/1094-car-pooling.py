class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capa={}
        enter={}
        out={}
        for i in trips:
            capa[i[0]]=1
            if i[1] in enter:
                enter[i[1]]+=i[0]
            else:
                enter[i[1]]=i[0]
            if i[2] in out:
                out[i[2]]+=i[0]
            else:
                out[i[2]]=i[0]
        z=max(out)
        x=0
        for i in range(z):
            if i in enter:
                x+=enter[i]
            if i in out:
                x-=out[i]
            if x>capacity:
                return False
        return True
            
        
                