class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0" or (row, col) in visited:
                return

            visited.add((row, col))
            
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
        
        print(visited)
        return islands




        
        