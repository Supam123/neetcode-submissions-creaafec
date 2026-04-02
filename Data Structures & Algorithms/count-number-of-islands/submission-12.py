class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        def dfs(r,c):
            if(r<0 or c<0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c]=="0" ):
                return 0
            
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1' and (r,c) not in visit):
                    counter +=1
                    dfs(r,c)
        return counter
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # visit = set()
        # rows,cols = len(grid),len(grid[0])
        # q = deque()

        # def bfs(r,c):
        #     directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #     q.append((r,c))
        #     visit.add((r,c))
        #     while q:
        #         r,c = q.popleft()
        #         for dr,dc in directions:
        #             nr,nc = r+dr,c+dc
        #             if(nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit or grid[nr][nc]=='0'):
        #                 continue
        #             q.append((nr,nc))
        #             visit.add((nr,nc))
        #     return
        # island_count = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if(grid[r][c] == '1' and (r,c) not in visit):
        #             bfs(r,c)
        #             island_count+=1
        # return island_count



        
       

        