class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows,cols =  len(matrix),len(matrix[0])
        def dfs(r,c):
            if r <0 or c<0 or r == rows or c== cols:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            res = 1
            # look down
            if  r+1< rows and matrix[r][c] < matrix[r+1][c]:
                res =  max(res,1+dfs(r+1,c))   
            # look up
            if  r-1 > -1 and matrix[r][c] < matrix[r-1][c]:
                res =  max(res,1+dfs(r-1,c))   
            # look right
            if  c+1 < cols and matrix[r][c] < matrix[r][c+1]:
                res =  max(res,1+dfs(r,c+1))   
            # look left
            if  c-1 > -1 and matrix[r][c] < matrix[r][c-1]:
                res =  max(res,1+dfs(r,c-1)) 
            memo[(r,c)] =  res
            return memo[(r,c)] 



        for r in range(rows):
            for c in range(cols):
                dfs(r,c)
        return max(memo.values())
             