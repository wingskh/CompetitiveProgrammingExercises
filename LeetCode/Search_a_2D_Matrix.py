# https://leetcode.com/problems/search-a-2d-matrix/submissions/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left_index, right_index = 0, m*n - 1
        middle_value = matrix[left_index//m][left_index%m]
        while left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            middle_value = matrix[middle_index//n][middle_index%n]

            if middle_value == target:
                return True
            if middle_value > target:
                right_index = middle_index 
            else:
                left_index = middle_index + 1

        return matrix[right_index//n][right_index%n] == target
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left_index, right_index = 0, m*n - 1
        middle_value = matrix[left_index//m][left_index%m]
        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            middle_value = matrix[middle_index//n][middle_index%n]
            if middle_value == target:
                return True
            if middle_value > target:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1]]
# matrix = [[1,3]]
target = 13
sol = Solution()
result = sol.searchMatrix(matrix, target)
print(result)