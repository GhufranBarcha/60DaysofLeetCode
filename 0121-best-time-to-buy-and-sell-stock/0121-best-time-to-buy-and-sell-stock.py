class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        ## Optimal way(I am idiot)

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:

            max_profit = max(max_profit , price - min_price)
            min_price = min(min_price ,price)

        return max_profit    


        # ## Brute force (but time limit exceed for larger values)
        # profit = 0

        # for i in range(len(prices)):
        #     pr = 0    
        #     for j in range(i+1 ,len(prices)):
        #         pr = prices[j] -prices[i]
        #         if profit <=  pr and pr > 0:
        #             profit = pr

        # return profit            
      




        