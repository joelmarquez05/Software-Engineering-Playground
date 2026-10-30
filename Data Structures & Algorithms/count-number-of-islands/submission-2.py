class Solution:
    def isValidPosition(self, row, col, ROWS, COLS):
        return 0 <= row <= ROWS-1 and 0 <= col <= COLS-1

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            
            for direction in directions:
                row_direction, col_direction = direction
                dfs(row + row_direction, col + col_direction)
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands




        
        