# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_row = len(matrix)
        max_col = len(matrix[0])
        
        r_index = max_row - 1
        c_index = 0
        while True:
            if c_index >= max_col or c_index < 0 or r_index >= max_row or r_index < 0:
                return False
            if matrix[r_index][c_index] == target:
                return True
            elif matrix[r_index][c_index] < target:
                c_index += 1
            else:
                r_index -= 1

        return False
