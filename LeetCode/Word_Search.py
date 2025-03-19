# https://leetcode.com/problems/word-search/
from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    # Non-recursion
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

    # Recursion
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(r, c):
            return True if r >= 0 and c >= 0 and r < row and c < col else False

        def dfs(r, c, index):
            if index == total_word:
                return True
 
            found_word = False
            for i in range(4):
                adj_row, adj_col = r + direction[i][0], c + direction[i][1]
                if (adj_row, adj_col) not in seen and is_valid(adj_row, adj_col) and board[adj_row][adj_col] == word[index]:
                    seen.add((adj_row, adj_col))
                    if dfs(adj_row, adj_col, index + 1):
                        found_word = True
                        break
                    seen.remove((adj_row, adj_col))

            return found_word

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_word = len(word)
        row, col = len(board), len(board[0])

        for r in range(row):
            for c in range(col):
                seen = set(((r, c),))
                if board[r][c] == word[0] and dfs(r, c, 1):
                   return True

        return False
         
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
# Output = True               
# board = [
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
# ]
# word = "AAAAAAAAAAAABAA"
# Output = False
board = [["a","a"]]
word = "aaa"
# Output = False
sol = Solution()
result = sol.exist(board, word)
print(result)
