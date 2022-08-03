# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num_of_rows = len(matrix)
        min_value = matrix[0][0]
        max_value = matrix[-1][-1]

        while min_value < max_value:
            mid_value = min_value + int(max_value - min_value) / 2
            if self.countSmallerThanMid(matrix, mid_value, num_of_rows) < k:
                min_value = mid_value + 1
            else:
                max_value = mid_value

        return min_value
    
    
    def countSmallerThanMid(self, matrix, mid_value, num_of_rows):
        column = num_of_rows - 1
        row = 0
        count = 0
        while column >= 0 and row < num_of_rows:
            if matrix[row][column] <= mid_value:
                count += column + 1
                row += 1
            else:
                column -= 1
        
        return count

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
sol = Solution()
print(sol.kthSmallest(matrix, k))
