class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        rows,cols = len(height),len(height[0])
        pac,atl = set(), set()

        def dfs(r,c,visit,prevHt):
            if r<0 or c<0 or r == rows or c== cols or (r,c) in visit  or height[r][c] < prevHt:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,height[r][c])
            dfs(r-1,c,visit,height[r][c])
            dfs(r,c+1,visit,height[r][c])
            dfs(r,c-1,visit,height[r][c])

        for c in range(cols):
            dfs(0,c,pac,height[0][c])
            dfs(rows-1,c,atl,height[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pac,height[r][0]) #left edge pacific

            dfs(r,cols-1,atl,height[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        