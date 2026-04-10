class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            set_rows=set()
            set_cols=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in set_rows:
                        return False
                    else:
                        set_rows.add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in set_cols:
                        return False
                    else:
                        set_cols.add(board[j][i])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                block_set=set()
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y]!='.':
                            if board[x][y] in block_set:
                                return False
                            else:
                                block_set.add(board[x][y])
        return True