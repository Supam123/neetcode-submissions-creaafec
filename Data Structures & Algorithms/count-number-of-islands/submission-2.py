class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        
        rows,columns = len(grid),len(grid[0])
        islands = 0
        visited = set()


        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            directions = [[0,-1],[0,1],[1,0],[-1,0]]
            q.append((r,c))
            while q:
                r,c = q.popleft()
                # now we wanna go in all four adjacent directions 
                for dr,dc in directions:
                    if(
                    r+dr in range(rows) and  # if index is valid
                    c+dc in range(columns) and # if index is valid
                    grid[r+dr][c+dc] == '1' and # if its a 1
                    (r+dr,c+dc) not in visited  # if this land is already not visited    
                    ):
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))
        for r in range(rows):
            for c in range(columns):
                if(grid[r][c] == '1') and (r,c) not in visited:
                    bfs(r,c) # we will mark islands visited inside this fucntion
                    islands+=1
        return islands
        