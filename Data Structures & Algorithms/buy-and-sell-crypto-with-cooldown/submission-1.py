class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        def dfs(i,buying):
            if i >= len(prices):
                return 0 #stock market closed 0 profit to be made
            if (i,buying) in memo:
                return memo[(i,buying)]
            
            if buying == False: 
                memo[(i,buying)] = max(-prices[i]+dfs(i+1,True),dfs(i+1,False))
            else:
                memo[(i,buying)] = max(prices[i]+dfs(i+2,False),dfs(i+1,True))
            return memo[(i,buying)]
        return dfs(0,False)


        