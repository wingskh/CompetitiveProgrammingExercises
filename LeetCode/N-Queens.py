# https://leetcode.com/problems/n-queens/
class InvalidLocation(Exception):
    pass


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queen_counter, board, available_rows):
            nonlocal n, result
            if queen_counter == n:
                result.append([board[i : i + n] for i in range(0, len(board), n)])
                return

            tmp_board = board
            for row in available_rows:
                valid = True
                try:
                    for i in range(n):
                        if tmp_board[(row * n) + i] != ".":
                            valid = False
                            raise InvalidLocation()

                    min_row_col = min(row, queen_counter)
                    tmp_row, tmp_col = row - min_row_col, queen_counter - min_row_col
                    max_row_col = max(tmp_row, tmp_col)
                    for i in range(n - max_row_col):
                        if tmp_board[((tmp_row + i) * n) + (tmp_col + i)] != ".":
                            valid = False
                            raise InvalidLocation()

                    total_diagonal = row + queen_counter + 1
                    if total_diagonal >= n:
                        extra = total_diagonal - n
                        tmp_row, tmp_col = extra, total_diagonal - extra - 1
                        total_diagonal = n - extra
                    else:
                        tmp_row, tmp_col = 0, total_diagonal - 1

                    for i in range(total_diagonal):
                        if tmp_board[((tmp_row + i) * n) + (tmp_col - i)] != ".":
                            valid = False
                            raise InvalidLocation()
                except InvalidLocation:
                    pass

                if valid:

                    tmp_board = (
                        board[: (row * n) + queen_counter]
                        + "Q"
                        + board[(row * n) + queen_counter + 1 :]
                    )
                    dfs(
                        queen_counter + 1,
                        tmp_board,
                        list(range(row - 1)) + list(range(row + 2, n)),
                    )
                else:
                    continue

        board = "." * n * n
        result = []
        dfs(0, board, list(range(n)))
        return result
