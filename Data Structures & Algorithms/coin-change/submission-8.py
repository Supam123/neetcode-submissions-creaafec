class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(capacity):
            if capacity == 0:
                return 0
            if capacity < 0:
                return float('inf')
            if capacity in memo:
                return memo[capacity]
            best =  float('inf')
            for c in coins:
                best = min(best,1+dp(capacity-c))
            memo[capacity] = best
            return  memo[capacity]
        answer = dp(amount)
        return -1 if answer == float('inf') else answer
