class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        dp = [0]*cols
        dp[cols-1] = 1 

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if(grid[r][c] == 1):
                    dp[c] = 0
                elif( c+1 <cols):
                    dp[c] = dp[c]+dp[c+1]
        return dp[0]
           

        # rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        # cache = [[0]*cols for _ in range(rows)]
        # def dfs(r,c):
        #     if(r==rows or c==cols or obstacleGrid[r][c] == 1 ):
        #         return 0
        #     if(r==rows-1 and c==cols-1):
        #         return 1
        #     if( cache[r][c] > 0):
        #         return cache[r][c]
            
        #     cache[r][c] = dfs(r+1,c)+dfs(r,c+1)

        #     return cache[r][c]
        # return dfs(0,0)
        # if (obstacleGrid[0][0]==1):
        #     return 0
        # rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        # prevRow = [0] * cols
        # for r in range(rows-1,-1,-1):
        #     currRow = [0] * cols
        #     for c in range(cols-1,-1,-1):
        #         if(r==rows-1 and c == cols-1):
        #             currRow[c] = 1 # this means we are the end destination
        #         elif(obstacleGrid[r][c]==1):
        #             currRow[c] = 0
        #         else:
        #             if(c+1 >= cols ):
        #                 val = 0
        #             else:
        #                 val = currRow[c+1]
        #             currRow[c] = prevRow[c]+ val 

        #     prevRow=currRow
        # return currRow[0]



        
















      

        