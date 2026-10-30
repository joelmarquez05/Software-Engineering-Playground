class Solution:

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isValidPosition(self, row, col, ROWS, COLS):
        return 0 <= row <= ROWS-1 and 0 <= col <= COLS-1

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(row, col):
            if not self.isValidPosition(row, col, ROWS, COLS) or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            
            for direction in self.directions:
                row_direction, col_direction = direction
                dfs(row + row_direction, col + col_direction)
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands




        
        