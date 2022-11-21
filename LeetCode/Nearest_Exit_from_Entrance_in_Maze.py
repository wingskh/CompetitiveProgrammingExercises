# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_valid(row, col):
            return (
                True
                if row >= 0
                and col >= 0
                and row < row_len
                and col < col_len
                and maze[row][col] == "."
                else False
            )

        queue = deque()
        entrance_tuple = tuple(entrance)
        queue.append((entrance_tuple, 0))
        row_len = len(maze)
        col_len = len(maze[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set(entrance_tuple)

        while len(queue) > 0:
            node, step = queue.popleft()
            if node != entrance_tuple and (
                node[0] == 0
                or node[1] == 0
                or node[0] == row_len - 1
                or node[1] == col_len - 1
            ):
                return step
            elif maze[node[0]][node[1]] == ".":
                for i in range(4):
                    adj_row, adj_col = (
                        node[0] + direction[i][0],
                        node[1] + direction[i][1],
                    )

                    if is_valid(adj_row, adj_col) and (adj_row, adj_col) not in visited:
                        queue.append(((adj_row, adj_col), step + 1))
                        visited.add((adj_row, adj_col))

        return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
# maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
# entrance = [1, 0]
# maze = [[".","+"]]
# entrance = [0, 0]
maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+","+","."]]
entrance = [0,1]
sol = Solution()
result = sol.nearestExit(maze, entrance)
print(result)
