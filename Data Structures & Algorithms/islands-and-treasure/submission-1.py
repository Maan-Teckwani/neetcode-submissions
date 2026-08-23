class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        m=len(grid)
        n=len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit = [[False]*n for _ in range(m)]
            visit[r][c]=True
            count=0

            while q:
                for _ in range(len(q)):
                    row,col=q.popleft()
                    if grid[row][col]==0:
                            return count
                    for dr,dc in directions:
                        nr=row+dr
                        nc=col+dc
                        
                        if 0<=nr<m and 0<=nc<n and not visit[nr][nc] and grid[nr][nc]!=-1:
                            q.append((nr,nc))
                            visit[nr][nc]=True
                count+=1
            return INF


        for i in range(m):
            for j in range(n):
                if grid[i][j]==INF:
                    grid[i][j]=bfs(i,j)
        
        

        
        