class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            no=["1"]
            for i in range(1,n):
                new=""
                l=1

                for j in range(len(no[0])-1):
                    if no[0][j]==no[0][j+1]:
                        l=l+1

                    else:
                        new+=str(l)+no[0][j]
                        l=1
                new+=str(l)+no[0][-1]
                no[0]=new


                
            return no[0]