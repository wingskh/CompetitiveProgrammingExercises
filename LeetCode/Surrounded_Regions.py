# https://leetcode.com/problems/surrounded-regions/
from typing import List

ROW_DIRECTION = (0, 1, 0, -1)
COL_DIRECTION = (-1, 0, 1, 0)


class Solution:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.seen = set()

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

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.height = len(board)
        self.width = len(board[0])

        def dfs(row, col, past_location_set):
            is_surrounded = True
            for i in range(4):
                adj_row = row + ROW_DIRECTION[i]
                adj_col = col + COL_DIRECTION[i]
                if (adj_row, adj_col) in past_location_set:
                    continue

                past_location_set.add((adj_row, adj_col))
                is_valid = self.is_valid(adj_row, adj_col)
                self.seen.add((adj_row, adj_col))
                if not is_valid:
                    is_surrounded = False
                    continue

                if board[adj_row][adj_col] == "O":
                    is_surrounded &= dfs(adj_row, adj_col, past_location_set)

            return is_surrounded

        for row in range(self.height):
            for col in range(self.width):
                if (row, col) in self.seen:
                    continue

                self.seen.add((row, col))
                if board[row][col] == "O":
                    past_location_set = set([(row, col)])
                    is_surrounded = dfs(row, col, past_location_set)
                    self.seen |= past_location_set
                    if is_surrounded:
                        for seen_row, seen_col in past_location_set:
                            board[seen_row][seen_col] = "X"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
# Output = [
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "O", "X", "X"],
# ]
# board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
# Output = [
#     ["O", "O", "O"],
#     ["O", "O", "O"],
#     ["O", "O", "O"]
# ]

sol = Solution()
sol.solve(board)
for row in board:
    print(row)
