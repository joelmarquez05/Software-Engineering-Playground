from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands_found = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"

            while queue:
                i, j = queue.popleft()

                for dr, dc in directions:
                    new_i = i + dr
                    new_j = j + dc

                    if (
                        0 <= new_i < ROWS
                        and 0 <= new_j < COLS
                        and grid[new_i][new_j] == "1"
                    ):
                        grid[new_i][new_j] = "0"
                        queue.append((new_i, new_j))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands_found += 1
                    bfs(i, j)

        return islands_found