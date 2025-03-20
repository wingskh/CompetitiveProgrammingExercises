# https://leetcode.com/problems/max-area-of-island/
from typing import List

ROW_DIRECTION = (0, 1, 0, -1)
COL_DIRECTION = (-1, 0, 1, 0)


class Solution:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.max_area = 0
        self.seen = set()

    def is_valid(self, row, col):
        return (
            True
            if row >= 0
            and col >= 0
            and row < self.height
            and col < self.width
            and (row, col) not in self.seen
            else False
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])

        def dfs(row, col, acc_area):
            self.seen.add((row, col))

            for i in range(4):
                adj_row = row + ROW_DIRECTION[i]
                adj_col = col + COL_DIRECTION[i]
                if self.is_valid(adj_row, adj_col) and grid[adj_row][adj_col]:
                    acc_area += dfs(adj_row, adj_col, 1)

            self.max_area = max(self.max_area, acc_area)
            return acc_area

        for row in range(self.height):
            for col in range(self.width):
                if grid[row][col]:
                    dfs(row, col, 1)

        return self.max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
sol = Solution()
print(sol.maxAreaOfIsland(grid))
