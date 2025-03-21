# https://leetcode.com/problems/rotting-oranges/
from typing import List

ROW_DIRECTION = (0, 1, 0, -1)
COL_DIRECTION = (-1, 0, 1, 0)


class Solution:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.elapsed_minutes = 0
        self.last_rotten_oranges = set()
        self.first_orange_count = 0

    def is_valid(self, row, col):
        return (
            True
            if row >= 0
            and col >= 0
            and row < self.height
            and col < self.width
            and (row, col)
            else False
        )

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])

        for row in range(self.height):
            for col in range(self.width):
                if grid[row][col] == 2:
                    self.last_rotten_oranges.add((row, col))
                elif grid[row][col] == 1:
                    self.first_orange_count += 1

        def go_to_next_minute():
            updated_last_rotten_oranges = set()
            for row, col in self.last_rotten_oranges:
                for i in range(4):
                    adj_row = row + ROW_DIRECTION[i]
                    adj_col = col + COL_DIRECTION[i]
                    if self.is_valid(adj_row, adj_col) and grid[adj_row][adj_col] == 1:
                        self.first_orange_count -= 1
                        grid[adj_row][adj_col] = 2
                        updated_last_rotten_oranges.add((adj_row, adj_col))

            if not len(updated_last_rotten_oranges):
                return -1 if self.first_orange_count else self.elapsed_minutes

            self.last_rotten_oranges = updated_last_rotten_oranges
            self.elapsed_minutes += 1
            return go_to_next_minute()

        return go_to_next_minute()


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
sol = Solution()
print(sol.orangesRotting(grid))
