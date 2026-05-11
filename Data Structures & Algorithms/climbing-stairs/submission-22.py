class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 1: # base case 0 or 1  
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] =  dfs(i-1) +dfs(i-2)
            return memo[i]
        return dfs(n)
      
            


     
        