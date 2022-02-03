class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x=version1.split('.')
        y=version2.split('.')
        for i in range(min(len(x),len(y))):
            if int(x[i])>int(y[i]):
                return 1
            if int(x[i])<int(y[i]):
                return -1
        d=len(x)
        f=len(y)
        print(x,y)
        if d==f:
            return 0
        else:
            if d>f:
                for i in range(d-f):
                    if int(x[d-i-1])>0:
                        return 1
            else:
                for i in range(f-d):
                    if int(y[f-i-1])>0:
                        return -1
        return 0
        