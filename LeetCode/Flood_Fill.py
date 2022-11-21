# https://leetcode.com/problems/flood-fill/
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def is_valid(row, col):
            return True if -1 < row < max_row and -1 < col < max_col and image[row][col] == ori_color else False

        ori_color = image[sr][sc]
        if ori_color == color:
            return image

        max_row = len(image)
        max_col = len(image[0])
        stack = deque([(sr, sc)])
        direction = [(1, 0), (-1, 0), (0, 1),(0, -1)]

        while len(stack) != 0:
            sr, sc = stack.pop()
            image[sr][sc] = color

            for i in range(4):
                adj_row, adj_col = sr + direction[i][0], sc + direction[i][1] 
                if is_valid(adj_row, adj_col):
                    stack.append((adj_row, adj_col))

        return image


image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2
sol = Solution()
result = sol.floodFill(image, sr, sc, color)
print(result)