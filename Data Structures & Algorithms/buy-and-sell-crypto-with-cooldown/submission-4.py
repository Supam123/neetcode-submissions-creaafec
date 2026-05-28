class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        empty_tmrw = 0
        holding_tmrw = 0
        empty_day_after = 0
        for i in range(len(prices)-1,-1,-1):
            curr_empty = max(-prices[i]+holding_tmrw,empty_tmrw)
            curr_holding = max(prices[i]+empty_day_after,holding_tmrw)

            empty_day_after = empty_tmrw # why ?

            empty_tmrw = curr_empty
            holding_tmrw = curr_holding
        return empty_tmrw # what to return fuck

    # dp_empty = [0] * (len(prices) + 2)
    # dp_holding = [0] * (len(prices) + 2)

    # for i in range(len(prices) - 1, -1, -1):
    #     # dp_empty[i]: Hands are empty.
    #     # Choice 1: Buy today. Pay price, move to 'holding' tomorrow.
    #     # Choice 2: Skip today. Move to 'empty' tomorrow.
    #     dp_empty[i] = max( -price[i] + dp_holding[i+1] , dp_empty[i+1] )
    #     # dp_holding[i]: Holding a stock.
    #     # Choice 1: Sell today. Get price, move to 'empty' the DAY AFTER tomorrow (cooldown).
    #     # Choice 2: Skip today. Move to 'holding' tomorrow.
    #     dp_holding[i] = max( price[i]+dp_empty[i+2] , dp_holding[i+1])





















        # memo = {}
        # def dfs(i,buying):
        #     if i >= len(prices):
        #         return 0 #stock market closed 0 profit to be made
        #     if (i,buying) in memo:
        #         return memo[(i,buying)]
            
        #     if buying == False: 
        #         memo[(i,buying)] = max(-prices[i]+dfs(i+1,True),dfs(i+1,False))
        #     else:
        #         memo[(i,buying)] = max(prices[i]+dfs(i+2,False),dfs(i+1,True))
        #     return memo[(i,buying)]
        # return dfs(0,False)


        