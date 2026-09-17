class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        visit=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()

           

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nc<0 or nr==n or nc==m or (nr,nc) in visit or grid[nr][nc]==-1:
                        continue
                    visit.add((nr,nc))
                    q.append([nr,nc])

            dist+=1

        
        
                        
        
        