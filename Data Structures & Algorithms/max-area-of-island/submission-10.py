class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area  = 0
        rows,cols = len(grid),len(grid[0])
        visit = set()
        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit or grid[r][c] == 0:
                return 0
            area = 1
            visit.add((r,c))
            area += dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    curr_area = dfs(r,c)
                    area = max(curr_area,area)
        return area

        