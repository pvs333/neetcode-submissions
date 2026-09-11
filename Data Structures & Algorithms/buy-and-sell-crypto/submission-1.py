class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0

        while r < len(prices):
            while prices[r] < prices[l]:
                l=r
                r+=1
                if(r==len(prices)):
                    return p
            p = max(p,prices[r]-prices[l])
            r+=1

        return p
        