class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
      
        rows,cols = len(grid),len(grid[0])
        visited = set ()
        q = deque()
        visited.add((0,0))
        q.append((0,0))
        length = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if( r== rows-1 and c == cols-1):
                    return length
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr,nc =  r+dr,c+dc
                    if(nr in range(rows)and nc in range(cols)and (nr,nc) not in visited and grid[nr][nc] == 0):
                        q.append((nr,nc))
                        visited.add((nr,nc))
            length+=1        
        return -1



        
        