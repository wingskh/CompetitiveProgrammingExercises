# https://leetcode.com/problems/valid-sudoku/
from typing import str, bool, List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in square_set[(r // 3, c // 3)]:
                    return False

                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                square_set[(r // 3, c // 3)].add(board[r][c])

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
k = 2
sol = Solution()
print(sol.isValidSudoku(board))
