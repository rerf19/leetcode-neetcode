class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range (9):
                if(board[r][c] != '.'):
                    if( board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[r//3,c//3] ):
                        return False
                    else:
                        cols[c].add(board[r][c])
                        rows[r].add(board[r][c])
                        boxes[(r // 3, c // 3)].add(board[r][c])
                else:
                    continue
        
        return True