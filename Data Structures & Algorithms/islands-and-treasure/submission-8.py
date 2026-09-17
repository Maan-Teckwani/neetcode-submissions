class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        visit=set()
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        n=len(grid)
        m=len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        
        dist=0
        while q:
            for _ in range(len(q)):
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


        
        
                        
        
        