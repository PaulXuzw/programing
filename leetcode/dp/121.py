class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        else:
            min = prices[0]
            maxProfit = 0
            for i in range(1,len(prices)):
                if prices[i]<min:
                    min = prices[i]
                else:
                    if prices[i]-min > maxProfit:
                        maxProfit = prices[i]-min
            return maxProfit
