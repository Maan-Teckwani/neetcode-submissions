class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        m=len(grid)
        n=len(grid[0])
        def bfs(r,c):
            q = collections.deque()
            visit=[[False] * n for _ in range(m)]
            visit[r][c]=True
            q.append((r,c))
            count=0
            while q:
                for _ in range(len(q)):
                    row,col=q.popleft()
                    if grid[row][col]==0:
                        return count
                    for dr,dc in directions:
                        nr,nc=row+dr,col+dc
                        if (0<=nc<n and 0<=nr<m and grid[nr][nc]!=-1 and not visit[nr][nc]):
                            visit[nr][nc]=True
                            q.append((nr,nc))
                count+=1
            return INF






        for i in range(m):
            for j in range(n):
                if grid[i][j]==INF:
                    grid[i][j]=bfs(i,j)
        
        

        
        