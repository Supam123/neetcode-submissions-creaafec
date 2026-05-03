class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                r,c =q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr<0 or nc<0 or nr == rows or nc==cols or (nr,nc) in visit or grid[nr][nc] ==-1:
                        continue
                    visit.add((nr,nc))
                    q.append((nr,nc))
                
                    grid[nr][nc] = grid[r][c] + 1
        
                    