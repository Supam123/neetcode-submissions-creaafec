class Solution:
    def climbStairs(self, n: int) -> int:
        #1st approach caching
        # cache = [-1]*n
        # def dfs(i):
        #     if(i>=n):
        #         return i==n
        #     if(cache[i] != -1):
        #         return cache[i]
        #     cache[i] = dfs(i+1)+dfs(i+2)
        #     return cache[i]
        # return dfs(0)
        one ,two=1,1
        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp
        return one

        