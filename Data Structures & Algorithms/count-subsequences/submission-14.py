class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i,j):
            if  j == len(t):
                return 1
            if i == len(s) and j != len(t):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            take,skip = 0,0
            if s[i] == t[j]:
                take = dp(i+1,j+1)
            skip = dp(i+1,j)
            memo[(i,j)] = take + skip
            return memo[(i,j)]
        return dp(0,0) 

