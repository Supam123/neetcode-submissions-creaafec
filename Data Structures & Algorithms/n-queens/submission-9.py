class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]
        cols = set()
        postDiag = set() # r+c
        negDiag = set() # r-c
        def dfs(r):
            #board looks like this
            '''
            [.,.,.q] -> ...q
            [q,.,.,.] - > q...
            final is [...q,q...]
            '''
            if r == n:
                res.append(["".join(row) for row in board])
                return 
            for c in range(n):
                if c in cols or (r+c) in postDiag or (r-c) in negDiag:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                postDiag.add((r+c))
                negDiag.add((r-c))
                dfs(r+1)
                board[r][c] = '.'
                cols.remove(c)
                postDiag.remove((r+c))
                negDiag.remove((r-c))
        dfs(0)
        return  res


            
        