class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text1),len(text2)
        cache = [[-1]*cols for _ in range(rows)]
        def dfs(i,j):
            if(i==len(text1) or j==len(text2)):
                return 0
            if(cache[i][j] >-1):# is already calculated
                return cache[i][j]
            if(text1[i]==text2[j]):
                cache[i][j] = 1+dfs(i+1,j+1)
            else:
                cache[i][j] = max(dfs(i+1,j),dfs(i,j+1))
            
            return cache[i][j]
        return dfs(0,0)




















        # rows,cols  = len(text1),len(text2)
        # dp = [  [0 for _ in range(cols+1)] 
        #         for _ in range(rows+1)]
        # for i in range(rows-1,-1,-1):
        #     for j in range(cols-1,-1,-1):
        #         if(text1[i] == text2[j]):
        #             dp[i][j] = 1+dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        # return dp[0][0]

        # rows,cols = len(text1),len(text2)
        # cache = [[-1]* cols for _ in range(rows)]
        # def dfs(i,j):
        #     if(i==rows or j==cols):
        #         return 0
        #     if(cache[i][j] >-1): 
        #         return cache[i][j]
            
        #     if(text1[i]==text2[j]):
        #         cache[i][j] = 1+dfs(i+1,j+1)
        #     else:
        #         cache[i][j] = max(dfs(i+1,j),dfs(i,j+1))
        #     return cache[i][j]
        
        # return dfs(0,0)


            
            


        