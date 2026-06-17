class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            
            while r < len(prices) and prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
            
            l += 1        
            r = l + 1
        return max_profit