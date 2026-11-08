from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 rows, 9 cols and board[i][j] will be ["1"..."9" or "."]

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                num = int(board[r][c])
                bit = 1 << num-1

                box_row = r // 3
                box_col = c // 3
                box_index = 3* box_row + box_col
                
                if (
                    rows[r] & bit
                    or cols[c] & bit
                    or boxes[box_index] & bit
                ):
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[box_index] |= bit
        
        return True



        
        



        