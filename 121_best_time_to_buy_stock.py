class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = prices[0]
        m = 0
        for i in range(1,len(prices)):
            if s > prices[i]:
                s = prices[i]
            elif prices[i] - s > m:
                m = prices[i] - s
        
        return m
        
