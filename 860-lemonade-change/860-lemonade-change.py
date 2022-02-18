class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        w={10:0,5:0}
        for i in bills:
            if i==20:
                if w[10]>0 and w[5]>0:
                    w[10]-=1
                    w[5]-=1
                elif w[5]>2:
                    w[5]-=3
                else:
                    return False
            if i==5:
                w[5]+=1
            if i==10:
                w[10]+=1
                if w[5]>0:
                    w[5]-=1
                else:
                    return False
        return True
                    
        