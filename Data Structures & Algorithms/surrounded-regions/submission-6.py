class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])

        def dfs(r,c):
            if r<0 or c < 0 or r ==  rows or c == cols or  board[r][c] == 'T' or board[r][c] == 'X':
                return
            board[r][c] = 'T' #meaning it was an O that can be visited from edges
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for c in range(cols): 
            dfs(0,c) # top
            dfs(rows-1,c) #bottom
        for r in range(rows):
            dfs(r,0)#left
            dfs(r,cols-1)#right

        # we have T (O that are touching edges)
        # we have X 
        # we have unotuched O --> need to turn to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        