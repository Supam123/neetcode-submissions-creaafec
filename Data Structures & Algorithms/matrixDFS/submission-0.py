class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r,c,grid,visited):
            if(min(r,c) <0 or r == len(grid) or c == len(grid[0])
             or grid[r][c] == 1 or (r,c) in visited):
                return 0
            if( r == len(grid)-1 and c == len(grid[0])-1):
                return 1
            visited.add((r,c))
            count = 0
            count += dfs(r+1,c,grid,visited)
            count += dfs(r,c+1,grid,visited)
            count += dfs(r-1,c,grid,visited)
            count += dfs(r,c-1,grid,visited)
            visited.remove((r,c))
            return count
        return dfs(0,0,grid,set())

        