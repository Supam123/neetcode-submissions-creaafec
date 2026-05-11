class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def dfs(i):
        #     #BASE CASE 
        #     if i <= 1: # base case 0 or 1  
        #         return 1
        #     # CACHING
        #     if i in memo:
        #         return memo[i]
        #     #STORING THE RESULT IN CACHE
        #     memo[i] =  dfs(i-1) +dfs(i-2)
            
        #     return memo[i]
        # return dfs(n)

        if n <= 1:
            return 1
        one_step_back = 1
        two_step_back = 1
        for i in range(2,n+1):
            curr_steps  = one_step_back + two_step_back
            two_step_back = one_step_back
            one_step_back = curr_steps
        return one_step_back
        






      
            


     
        