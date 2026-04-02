class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHm = { r: set() for r in range(len(board))}
        colHm = { c: set() for c in range(len(board[0]))}
        boxesHm = {(r,c) :set() for r in range(3) for c in range(3)}
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(board[r][c] != '.'):
                    if board[r][c] not in rowHm[r]:
                        rowHm[r].add(board[r][c])
                    else:
                        return False
                    
                    if board[r][c] not in colHm[c]:
                        colHm[c].add(board[r][c])
                    else:
                        return False
            
                    if board[r][c] not in boxesHm[(r//3,c//3)]:
                        boxesHm[(r//3,c//3)].add(board[r][c])
                    else:
                        return False
        return True
        