class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # row_below = [0]*(amount+1)
        # for i in range(len(coins)-1,-1,-1):
        #     curr_row= [0]*(amount+1)
        #     curr_row[0] = 1
        #     for cap in range(1,amount+1):
        #         skip = row_below[cap]
        #         take = 0
        #         if cap - coins[i] >=0:
        #             take = curr_row[cap - coins[i]]
        #         curr_row[cap] = take+skip
        #     row_below = curr_row
        # return row_below[-1]



















        # 1. Create the empty 2D grid filled with 0s
        # (This automatically handles our "i >= len(coins)" base case row!)
        grid = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # 2. Fill the "capacity == 0" base case column with 1s
        for i in range(len(coins) + 1):
            grid[i][0] = 1

        # 3. The nested loops to traverse the grid
        # Start at the bottom row (len(coins) - 1) and move UP to row 0
        for i in range(len(coins) - 1, -1, -1):
   
            # Move across the columns from left to right (cap 1 to amount)
            for cap in range(1, amount + 1):
   
                # The "SKIP" choice (Look DOWN)
                skip = grid[i + 1][cap]
   
                # The "TAKE" choice (Look LEFT)
                # We must check if looking left keeps us on the board!
                take = 0
                if cap - coins[i] >= 0:
                    take = grid[i][cap - coins[i]]
   
                # Total ways for this box
                grid[i][cap] = skip + take
   
        # 4. The final answer is in the top-right box
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

                                                                                                                                                                                    