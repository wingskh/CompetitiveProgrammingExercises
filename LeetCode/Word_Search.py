# https://leetcode.com/problems/word-search/
from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(row, col):
            return (
                True
                if row >= 0 and col >= 0 and row < total_row and col < total_col
                else False
            )

        sources = []
        total_row = len(board)
        total_col = len(board[0])
        last_word_index = len(word) - 1

        if total_row * total_col <= last_word_index:
            return False

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        board_counter = defaultdict(int)
        for row in range(total_row):
            for col in range(total_col):
                board_counter[board[row][col]] += 1
                if board[row][col] == word[0]:
                    sources.append((row, col))

        word_counter = Counter(list(word))
        for w in set(word):
            if board_counter[w] < word_counter[w]:
                return False

        if last_word_index == 0 and len(sources) > 0:
            return True

        for source in sources:
            stack = []
            stack.append((source, 0, (-1, -1)))
            seen = []
            seen.append(source)

            while len(stack) != 0:
                x, index, last_x = stack.pop()
                seen = seen[: index + 1]
                seen.append(x)
                for i in range(4):
                    adj_row, adj_col = x[0] + direction[i][0], x[1] + direction[i][1]
                    if (
                        is_valid(adj_row, adj_col)
                        and (adj_row, adj_col) not in seen
                        and word[index + 1] == board[adj_row][adj_col]
                        and not (adj_row == last_x[0] and adj_col == last_x[1])
                    ):
                        if index + 1 == last_word_index:
                            return True
                        else:
                            stack.append(((adj_row, adj_col), index + 1, x))
        return False


board = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]
word = "AAAAAAAAAAAABAA"
sol = Solution()
result = sol.exist(board, word)
print(result)
