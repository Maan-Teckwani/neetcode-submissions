class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        fresh=0
        q=collections.deque()
        mins=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))

        while fresh>0 and q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1:
                        q.append((nr,nc))
                        fresh-=1
                        grid[nr][nc]=2
                        


            mins+=1

        if fresh==0:
            return mins
        else:
            return -1
