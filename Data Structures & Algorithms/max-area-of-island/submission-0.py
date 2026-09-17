class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        m=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(i,j,area):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
                return area
            grid[i][j]=0
            area+=1
            for dr,dc in directions:
                area=dfs(i+dr,j+dc,area)
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j,0))
        
        return ans
        