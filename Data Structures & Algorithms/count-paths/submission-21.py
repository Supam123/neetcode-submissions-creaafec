class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        # row_below = [1] * n
        # for r in range(m-2,-1,-1):
        #     curr_row = [1] * n
        #     for c in range(n-2,-1,-1):
        #         curr_row[c] = row_below[c] +curr_row[c+1]
        #     row_below = curr_row
        # return row_below[0]
                
                
        
        memo = {}
        def dfs(r,c):
            if  r>=m or c>=n :
                return 0
            if r == m-1 and c == n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return memo[(r,c)]
        return dfs(0,0)
         


