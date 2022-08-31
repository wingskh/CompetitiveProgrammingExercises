# https://leetcode.com/problems/pacific-atlantic-water-flow/
from collections import deque


class Solution:
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    def pacificAtlantic(self, heights):
        max_row = len(heights)
        max_col = len(heights[0])
        # row_direction = [0, 1, 0, -1]
        # col_direction = [-1, 0, 1, 0]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific_ocean_points = set()
        atlantic_ocean_points = set()

        def is_valid(row, col):
            if 0 <= row < max_row and 0 <= col < max_col:
                return True
            return False

        def dfs(cur_row, cur_col, visited):
            stack = deque([(cur_row, cur_col)])
            while len(stack) > 0:
                (cur_row, cur_col) = stack.pop()

                if (cur_row, cur_col) in visited:
                    continue
                visited.add((cur_row, cur_col))

                for i in range(4):
                    adj_row = cur_row + direction[i][0]
                    adj_col = cur_col + direction[i][1]
                    if (
                        (adj_row, adj_col) not in visited
                        and is_valid(adj_row, adj_col)
                        and heights[adj_row][adj_col] >= heights[cur_row][cur_col]
                    ):
                        stack.append((adj_row, adj_col))

        for i in range(max_row):
            dfs(i, 0, pacific_ocean_points)
            dfs(i, max_col - 1, atlantic_ocean_points)

        for i in range(max_col):
            dfs(0, i, pacific_ocean_points)
            dfs(max_row - 1, i, atlantic_ocean_points)

        return pacific_ocean_points.intersection(atlantic_ocean_points)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
sol = Solution()
result = sol.pacificAtlantic(heights)
print(result)
