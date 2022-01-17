class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=1000000
        ans=0
        for i in prices:
            if (i-min_price)>ans:
                ans=i-min_price
            if min_price>i:
                min_price=i
        return ans
        