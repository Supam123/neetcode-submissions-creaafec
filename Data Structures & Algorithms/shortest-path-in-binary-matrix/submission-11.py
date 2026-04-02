class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if(grid[0][0]==1): # NO PATHS 
            return -1
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        q.append((0,0))
        visit.add((0,0))
        length = 1

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if(r==rows-1 and c== cols-1):
                    return length
                
                directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],
                [-1,1],[1,-1],[-1,-1]]
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if(nr<0 or nc<0 or nr==rows or nc== cols or (nr,nc) in visit or grid[nr][nc]==1):
                        continue

                    q.append((nr,nc))
                    visit.add((nr,nc))
            length +=1
        return -1

        


        