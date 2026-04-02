class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

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
        if (obstacleGrid[0][0]==1):
            return 0
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        prevRow = [0] * cols
        for r in range(rows-1,-1,-1):
            currRow = [0] * cols
            for c in range(cols-1,-1,-1):
                if(r==rows-1 and c == cols-1):
                    currRow[c] = 1
                elif(obstacleGrid[r][c]==1):
                    currRow[c] = 0
                else:
                    if(c+1 >= cols ):
                        val = 0
                    else:
                        val = currRow[c+1]
                    currRow[c] = prevRow[c]+ val 

            prevRow=currRow
        return currRow[0]



        
















      

        