class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>= cols or (r,c) in visit or grid[r][c] == 0):
                return 0
            
            visit.add((r,c))
            return 1+ dfs(r+1,c) + dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)
      
        area = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1 and (r,c) not in visit ):
                    area = max(dfs(r,c),area)
        return area































        # rows,cols = len(grid),len(grid[0])
        # q = deque()
        # visit = set()
        # directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # area = 0
        # def bfs(r,c):
        #     a = 1
        #     q.append((r,c))
        #     visit.add((r,c))
        #     while q:
        #         r,c=q.popleft()
        #         for dr,dc in directions:
        #             nr,nc = dr+r,dc+c
        #             if(nr < 0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visit or grid[nr][nc]==0):
        #                 continue
        #             q.append((nr,nc))
        #             visit.add((nr,nc))
        #             a += 1
                
        #     return a
        # for r in range(rows):
        #     for c in range(cols):
        #         if(grid[r][c]==1):
        #             area = max(area,bfs(r,c))
        # return area



                






        