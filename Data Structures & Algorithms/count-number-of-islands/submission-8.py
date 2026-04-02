class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows,cols = len(grid),len(grid[0])
        q = deque()

        def bfs(r,c):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if(nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit or grid[nr][nc]=='0'):
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            return
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1' and (r,c) not in visit):
                    bfs(r,c)
                    island_count+=1
        return island_count



        
       

        