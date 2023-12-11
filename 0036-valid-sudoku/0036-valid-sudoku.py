class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        # Verify row
        for r in range(n):
            rowCheck = set()
            for c in range(n):
                s = board[r][c]
                if s in rowCheck:
                    return False
                else:
                    if s != ".":
                        rowCheck.add(s)
        
        # Verify Column
        for c in range(n):
            colCheck = set()
            for r in range(n):
                s = board[r][c]
                if s in colCheck:
                    return False
                else:
                    if s != ".":
                        colCheck.add(s)
        
        # Verify block
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                bloCheck = set()
                for i in range(3):
                    for j in range(3):
                        s = board[r+i][c+j]
                        if s in bloCheck:
                            return False
                        else:
                            if s != ".":
                                bloCheck.add(s)
                        print(bloCheck)
        
        return True