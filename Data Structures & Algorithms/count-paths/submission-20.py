class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_below = [1]*n
        for r in range(m-2,-1,-1):
            curr_row = [1]*n 
            for c in range(n-2,-1,-1):
                curr_row[c] = row_below[c] + curr_row[c+1]
            row_below = curr_row
        return row_below[0]    
