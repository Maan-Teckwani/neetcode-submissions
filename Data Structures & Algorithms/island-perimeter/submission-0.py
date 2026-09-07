class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perim=0
            for dr,dc in directions:
                perim+=dfs(i+dr,j+dc)
            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j)
        
        return 0




        