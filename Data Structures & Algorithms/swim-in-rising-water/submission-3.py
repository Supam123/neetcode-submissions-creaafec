class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        h = []
        visit = set()
        heapq.heappush(h,(grid[0][0],(0,0)))
      
        rows,cols = len(grid),len(grid[0])
        max_so_far = grid[0][0]
        while h:
            height,(r,c) =  heapq.heappop(h)
            if r == rows-1 and c==cols-1:
                return height
            if (r,c) in visit:
                continue
            visit.add((r,c))
            directions = [[0,1],[0,-1],[-1,0],[1,0]]
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if nr<0 or nc<0 or nr >= rows or nc>=cols or (nr,nc) in visit:
                    continue
                heapq.heappush(h, (max(height,grid[nr][nc]), (nr,nc)))




            