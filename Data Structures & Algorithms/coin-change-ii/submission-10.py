class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        grid = [[0]*(amount+1) for _ in range(len(coins)+1)]

        #when cap = 0 we return 1 from top down so we do that
        for i in range(0,len(coins)+1):
            grid[i][0] =1
        #bottom up 
        for i in range(len(coins)-1,-1,-1):
            for cap in range(1,amount+1):
                skip = grid[i+1][cap]
                take = 0
                if cap-coins[i] >= 0:
                    take = grid[i][cap-coins[i]]
                grid[i][cap] = take + skip
        return grid[0][amount]
                

        # memo = {}
        # def dp(i,capacity):
        #     if i >= len(coins):
        #         return 0
        #     if capacity == 0:
        #         return 1 # thats  one way existed existed
        #     if capacity < 0:
        #         return 0
        #     if (i,capacity) in memo:
        #         return memo[(i,capacity) ]
        #     take = dp(i,capacity-coins[i])
        #     skip = dp(i+1,capacity)
        #     memo[(i,capacity) ] = take + skip
        #     return memo[(i,capacity)]
        # return dp(0,amount)

                                                                                                                                                                                    