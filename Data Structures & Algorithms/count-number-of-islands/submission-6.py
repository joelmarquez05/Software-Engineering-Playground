class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_found = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        # i should be between [0, ROWS-1] => i < 0 or i > ROWS-1
        # j should be between [0, COLS-1] => j < 0 or j > COLS-1

        def dfs(i, j):
            if i < 0 or i > ROWS - 1 or j < 0 or j > COLS - 1 or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands_found += 1
                    dfs(i,j)
        return islands_found

        




        
        