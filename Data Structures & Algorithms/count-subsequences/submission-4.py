class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i,j):
            if j == len(t):
                return 1# we mactehd and reacehd end of the string
            if i == len(s):
                return 0# if i reached end of the string and j did not meanign no macth exhausted 0
            if (i,j) in memo:
                return memo[(i,j)]
            take,skip=0,0
            if s[i] == t[j]:
                take = dp(i+1,j+1)
            
     
            skip = dp(i+1,j)
            memo[(i,j)] =  take + skip
            return memo[(i,j)]
        return dp(0,0)
        