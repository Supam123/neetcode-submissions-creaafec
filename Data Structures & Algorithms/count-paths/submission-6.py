class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols = m,n
        prevRow = [0]*cols
        for i in range(rows-1,-1,-1):
            currRow = [0]*cols
            currRow[cols-1] = 1
            for j in range(cols-2,-1,-1):
                currRow[j] = currRow[j+1]+prevRow[j]
            prevRow = currRow
        
        return currRow[0]

    














        # rows,cols = m,n
        # dp = [0] * cols
        # dp[cols-1] = 1
        # for r in range(rows-1,-1,-1):
        #     for c in range(cols-1,-1,-1):
        #         if(c+1<cols):
        #             dp[c] =dp[c]+dp[c+1]
        # return dp[0]






        # rows  = m
        # cols = n
        # prevRows = [0]*cols
        # for _ in range(rows-1,-1,-1):
        #     currRow = [0]*cols
        #     currRow[cols-1] = 1
        #     for c in range(cols-2,-1,-1):
        #         currRow[c] = currRow[c+1] + prevRows[c]
        #     prevRows = currRow
        # return currRow[0]


        # cache = [[0] * n for _  in range(m)]
        # rows = m
        # cols = n
        # def dfs(r,c):
        #     if( r == rows or c == cols): 
        #         return 0 # out of bounds
        #     if(r == rows-1 and c == cols-1):
        #         return 1
            
        #     if( cache[r][c] > 0 ):
        #         return cache[r][c]
            
        #     cache[r][c] = dfs(r+1,c) + dfs(r,c+1)

        #     return cache[r][c]
        # return dfs(0,0)
        # cols = n
        # rows = m
        # prevRow = [0] * cols
        # for r in range(rows-1,-1,-1):
        #     currRow = [0]*cols
        #     currRow[cols-1] = 1
        #     for c in range(cols-2,-1,-1):
        #         currRow[c] = prevRow[c]+currRow[c+1]
            
        #     prevRow = currRow
        
        # return currRow[0]
























        
        