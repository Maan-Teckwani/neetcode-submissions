class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen=set()

            for i in range(9):
                if board[row][i]=='.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen=set()

            for j in range(9):
                if board[j][col]=='.':
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        num=board[i+box_row][j+box_col]
                        if num!='.':
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True

        
        