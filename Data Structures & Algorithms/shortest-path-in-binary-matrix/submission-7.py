class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        if(grid[0][0] == 1):
            return -1
        q.append((0,0))
        visit.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        def bfs(r,c):

            path = 1
            while q:
                for _ in range(len(q)): # we are doing level counting here not every cell counting
                    r,c = q.popleft()
                    if(r == rows-1 and c == cols-1):
                        return path
                    for dr,dc in directions:
                        nr,nc = dr+r,dc+c
                        if(nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==1  or (nr,nc) in visit):
                            continue
                        q.append((nr,nc))
                        visit.add((nr,nc))
                path+=1
            return -1
        return bfs(0,0)


        