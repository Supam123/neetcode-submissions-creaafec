class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)  # rows
        n = len(text2)  # cols
        '''
        c r a b t
    c              0
    a       2  1   1   0
    t   1 1 1 1 1  0
        0 0 0 0 0  0
        '''
        row_below = [0] * (n+1)
        for r in range(m-1,-1,-1):
            curr_row = [0] * (n+1)
            for c in range(n-1,-1,-1):
                if text1[r] == text2[c]:
                    curr_row[c] = 1 + row_below[c+1]
                else:
                    curr_row[c] = max(curr_row[c+1],row_below[c])
            row_below = curr_row
        return row_below[0]




















        # memo = {}
        # def dfs(i,j):
        #     if  i == len(text1) or j == len(text2):
        #         return 0
            
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if text1[i] == text2[j]:
        #         memo[(i,j)] = 1 + dfs(i+1,j+1)
        #     else:
        #         memo[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
        #     return memo[(i,j)]
        # return dfs(0,0)
        