class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[0] * n for _  in range(m)]
        rows = m
        cols = n
        def dfs(r,c):
            if( r == rows or c == cols): 
                return 0 # out of bounds
            if(r == rows-1 and c == cols-1):
                return 1
            
            if( cache[r][c] > 0 ):
                return cache[r][c]
            
            cache[r][c] = dfs(r+1,c) + dfs(r,c+1)

            return cache[r][c]
        return dfs(0,0)


        
        