# https://leetcode.com/problems/rotate-image/
# https://leetcode.com/problems/rotate-image/discuss/2503184/Python-oror-Easily-Understood-oror-Faster-than-99-oror-Less-than-99
import math


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(math.ceil(n / 2)):
            for col in range(int(n - n / 2)):
                (
                    matrix[row][col],
                    matrix[~col][row],
                    matrix[~row][~col],
                    matrix[col][~row],
                ) = (
                    matrix[~col][row],
                    matrix[~row][~col],
                    matrix[col][~row],
                    matrix[row][col],
                )
        return matrix


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol = Solution()
result = sol.rotate(matrix)
print(result)

# rotate a matrix
# [
# [7, 8, 1], 
# [6, 5, 4], 
# [9, 2, 3]
# ]