class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows,cols = len(grid),len(grid[0])
        def dfs(r,c):
            if(r < 0 or c<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c]=='0'):
                return 0
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=='1' and (r,c) not in visit):
                    dfs(r,c)
                    island_count+=1
        return island_count

        