class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        fresh=0
        q=deque()
        minutes=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i,j])

        while q and fresh:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr<R and nr>=0 and nc<C and nc>=0 and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append([nr,nc])
            minutes+=1
        if fresh==0:
            return minutes
        else:
            return -1
        