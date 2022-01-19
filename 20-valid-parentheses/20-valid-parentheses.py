class Solution:
    def isValid(self, s: str) -> bool:
        sa=[]
        if len(s)<=1:
            return False
        
        for i in s:
            if len(sa)>=1:
                if i=='[' or i=='(' or i=='{':
                    sa.append(i)
                else:
                    if i==']':
                        if sa[-1]=='[':
                            del sa[-1]
                        else:
                            return False
                    if i=='}':
                        if sa[-1]=='{':
                            del sa[-1]
                        else:
                            return False
                    if i==')':
                        if sa[-1]=='(':
                            del sa[-1]
                        else:
                            return False
            else:
                sa.append(i)
        if len(sa)==0:
            return True
        else:
            return False
                
                