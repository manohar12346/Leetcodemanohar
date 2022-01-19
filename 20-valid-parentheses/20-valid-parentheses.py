class Solution:
    def isValid(self, s: str) -> bool:
        sa=[]
        for i in s:
            if len(sa)>=1:
                if sa[-1]+i=="()" or sa[-1]+i=="[]" or sa[-1]+i=="{}":
                    del sa[-1]
                else:
                    sa.append(i)
            else:
                sa.append(i)
        if len(sa)==0:
            return True
        else:
            return False
                
                