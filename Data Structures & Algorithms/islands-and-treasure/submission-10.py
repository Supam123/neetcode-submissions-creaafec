class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        inf = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: #multi source bfs. 
                    q.append((r,c))
                    visit.add((r,c))
    #start multi source bfs
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                r,c =  q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr < 0 or nc < 0 or  nr == rows or nc == cols or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    if grid[nr][nc] == inf and grid[r][c] == 0: # first time 0 touches inf
                        grid[nr][nc] = 1
                    else:
                        grid[nr][nc] = grid[r][c] +  1 # previous value at the cell plus 1 for the current
                    q.append((nr,nc))
                    visit.add((nr,nc))



