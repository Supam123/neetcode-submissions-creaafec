class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()
        ROWS,COLS =  len(grid),len(grid[0])
        q.append((0,0))
        visit.add((0,0))
        length = 0
        while q:
            directions =[[0,1],[0,-1],[1,0],[-1,0]]
            for _ in range(len(q)):
                r,c = q.popleft()
                if(r == ROWS-1 and c==COLS-1):
                    return length
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if((nr,nc) not in visit and  nr>=0 and nc >=0 and nr<ROWS and nc<COLS and grid[nr][nc] == 0):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            length +=1
        return -1





        
        