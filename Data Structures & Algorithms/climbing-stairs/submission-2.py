class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if(i>=n):
                return i==n # if 5 == 5 return 1 else 0
            if(i in cache):
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
        
            return cache[i]

        return dfs(0)
        



        