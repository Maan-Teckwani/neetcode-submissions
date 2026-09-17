class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        visit=set()
        q=deque()

        def addCell(i,j):
            if i<0 or j<0 or i==n or j==m or (i,j) in visit or grid[i][j]==-1:
                return
            visit.add((i,j))
            q.append([i,j])

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
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist+=1

        
        
                        
        
        