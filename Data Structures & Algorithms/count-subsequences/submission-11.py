class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        row_below = [0]* (len(t)+1)
        row_below[-1] = 1
        for i in range(len(s)-1,-1,-1):
            curr_row = [0]* (len(t)+1)
            curr_row[-1] = 1
            for j in range(len(t)-1,-1,-1):
                take,skip=0,0
                if s[i] == t[j]:
                    take = row_below[j+1]
                skip = row_below[j]
                curr_row[j] = take+skip
            row_below = curr_row
        return row_below[0]
                














   
   
        # memo = {}
        # def dp(i,j):
        #     if j == len(t):
        #         return 1# we mactehd and reacehd end of the string
        #     if i == len(s):
        #         return 0# if i reached end of the string and j did not meanign no macth exhausted 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     take,skip=0,0
        #     if s[i] == t[j]:
        #         take = dp(i+1,j+1)
            
     
        #     skip = dp(i+1,j)
        #     memo[(i,j)] =  take + skip
        #     return memo[(i,j)]
        # return dp(0,0)
        