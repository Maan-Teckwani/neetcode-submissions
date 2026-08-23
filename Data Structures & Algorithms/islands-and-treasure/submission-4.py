class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=collections.deque()
        visit=set()

        def addCell(r,c):
            if min(r,c)<0 or r==m or c==n or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        
        dist=0
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist
                addCell(row+1,col)
                addCell(row,col+1)
                addCell(row-1,col)
                addCell(row,col-1)
            dist+=1
        
        

        
        