from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 rows, 9 cols and board[i][j] will be ["1"..."9" or "."]

        rows = defaultdict(set) # row number -> set with the seen numbers
        cols = defaultdict(set)
        boxes = defaultdict(set) #1-9

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box_row = r // 3
                col_row = c // 3
                
                if (
                    num in rows[r]
                    or num in cols[c]
                    or num in boxes[(box_row, col_row)]
                ):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[(box_row, col_row)].add(num)
        
        return True



        
        



        