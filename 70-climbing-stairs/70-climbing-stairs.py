class Solution:
    def climbStairs(self, n: int) -> int:
        # def climb(n):
        #     if n<=2:
        #         return n
        #     else:
        #         return climb(n-1)+climb(n-2)
        # return climb(n)
        ans=[1,2]
        if n==1:
            return 1
        for i in range(2,n):
            ans.append(ans[-1]+ans[-2])
        return ans[-1]