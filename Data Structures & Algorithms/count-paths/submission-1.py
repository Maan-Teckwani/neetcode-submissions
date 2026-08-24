class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[-1 for _ in range(n)] for _ in range(m)]
        directions = [[1,0],[0,1]]
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if grid[i][j]!=-1:
                return grid[i][j]
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            grid[i][j]=down+right
            return grid[i][j]
        return dfs(0,0)
            
        
        