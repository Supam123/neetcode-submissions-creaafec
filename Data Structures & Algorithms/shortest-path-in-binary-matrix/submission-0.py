class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS,COLS = len(grid),len(grid[0])
        visit =  set()
        q = deque()

        if(grid[0][0] == 1):
            return -1
        else:
            q.append((0,0))
            visit.add((0,0))
            count = 1

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if(r == ROWS-1 and c == COLS-1):
                    return count
                directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
                for dr,dc in directions:
                    nr,nc  = r+dr,c+dc
                    if(nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == 0  ):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            count +=1
        return -1

        