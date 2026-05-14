class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dfs(i,amt):
            if  amt == 0:
                return 0
            if amt < 0:
                return float('inf') # invalid path return impossible
            if i == len(coins):
                return float('inf')
            if (i,amt) in memo:
                return memo[(i,amt)]
            
            skip_res = dfs(i+1,amt)
            take_res = 1 + dfs(i, amt-coins[i])
            res = min(skip_res,take_res)
            memo[(i,amt)] = res
            return res
        return -1 if dfs(0,amount) == float('inf')   else  dfs(0,amount)

        
        