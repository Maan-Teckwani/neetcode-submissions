class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        pac,atl=set(),set()
        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r<0 or r>=m or c<0 or c>=n or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])



        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m-1,c,atl,heights[m-1][c])

        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1,atl,heights[r][n-1])
        
        return list(atl.intersection(pac))
        