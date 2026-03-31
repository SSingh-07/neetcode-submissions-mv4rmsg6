class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = len(board), len(board[0])
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '.':
                    continue

                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in grid[(r//3,c//3)]:
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grid[(r//3,c//3)].add(board[r][c])

        return True

        