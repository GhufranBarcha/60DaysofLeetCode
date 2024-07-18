class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            pr = 0    
            for j in range(i+1 ,len(prices)):
                pr = prices[j] -prices[i]
                if profit <=  pr and pr > 0:
                    profit = pr

        return profit            
      




        