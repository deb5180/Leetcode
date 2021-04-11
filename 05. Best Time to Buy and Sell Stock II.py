class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(1, len(prices)):
            if prices[index-1] < prices[index]:
                profit += (prices[index] - prices[index-1])
        
        return profit