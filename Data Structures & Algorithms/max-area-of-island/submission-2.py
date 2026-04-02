class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=[0]
        if(grid):
            rows,cols = len(grid),len(grid[0])
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            def bfs(r,c):
                q = deque()
                q.append((r,c))
                grid[r][c] = 0 # this is now visited
                number_of_islands =1

                while q:
                    r,c = q.popleft()
                    for dr,dc in directions:
                        nr, nc = r+dr, c+dc
                        if(nr in range(rows) and  nc in range(cols) and grid[nr][nc] ==1):
                            q.append((nr,nc))
                            number_of_islands +=1
                            grid[nr][nc] = 0
                area.append(number_of_islands)
                



            for r in range(rows):
                for c in range(cols):
                    if(grid[r][c] == 1):
                        bfs(r,c)
        return max(area)
        
        