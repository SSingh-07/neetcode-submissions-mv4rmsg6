class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = COL = 9
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '.':
                    continue

                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in grid[(i//3, j//3)]:
                    return False
                
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])

        return True
        