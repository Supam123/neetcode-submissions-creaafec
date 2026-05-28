class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i,capacity):
            if i >= len(coins):
                return 0
            if capacity == 0:
                return 1 # thats  one way existed existed
            if capacity < 0:
                return 0
            if (i,capacity) in memo:
                return memo[(i,capacity) ]
            take = dp(i,capacity-coins[i])
            skip = dp(i+1,capacity)
            memo[(i,capacity) ] = take + skip
            return memo[(i,capacity)]
        return dp(0,amount)

                                                                                                                                                                                    