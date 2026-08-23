class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        visit=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c,visit):
            if (r,c) in visit or r<0 or r>=m or c<0 or c>=n or board[r][c]=='X':
                return
            visit.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                dfs(nr,nc,visit)
        
        for c in range(n):
            if board[0][c]=='O':
                dfs(0,c,visit)
        
        for c in range(n):
            if board[m-1][c]=='O':
                dfs(m-1,c,visit)
        for r in range(m):
            if board[r][0]=='O':
                dfs(r,0,visit)
        
        for r in range(m):
            if board[r][n-1]=='O':
                dfs(r,n-1,visit)
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O' and (r,c) not in visit:
                    board[r][c]='X'
                

        
        