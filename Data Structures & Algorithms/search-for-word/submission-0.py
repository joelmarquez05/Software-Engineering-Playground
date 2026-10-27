class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows_length = len(board)
        cols_length = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()

        def valid_position(row, col):
            return 0 <= row < rows_length and 0 <= col < cols_length

        def backtrack(row, col, index):
            if not valid_position(row, col) or word[index] != board[row][col] or (row, col) in visited:
                return False
            if index == len(word) - 1:
                return True
            
            visited.add((row, col))
            for direction in directions:
                dir_x, dir_y = direction
                if backtrack(row + dir_x, col + dir_y, index + 1):
                    return True
            visited.remove((row, col))
            return False

        for i in range(rows_length):
            for j in range(cols_length):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False 
