# https://leetcode.com/problems/sort-the-matrix-diagonally/
# https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/2493821/python-easily-understood-faster-than-93-less-than-99

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        total_num = row * col

        for i in range(1, row + col - 2):
            if i < row:
                start_row, start_col = row - i - 1, 0
            else:
                start_row, start_col = 0, i - row + 1

            diag = []
            while start_row < row and start_col < col:
                diag.append(mat[start_row][start_col])
                start_row += 1
                start_col += 1

            diag.sort()
            start_row -= 1
            start_col -= 1
            while start_row >= 0 and start_col >= 0:
                mat[start_row][start_col] = diag.pop()
                start_row -= 1
                start_col -= 1

        return(mat)

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
sol = Solution()
result = sol.diagonalSort(mat)
print(result)


#       0   1   2   3   4   5
#       6   7   8   9   10  11   
#       12  13  14  15  16  17
#       18  19  20  21  22  23
# 
# 
#       0, 7, 14, 21 
#
#

#       0,0     0,1     0,2     0,3
#       1,0     1,1     1,2     1,3
#       2,0     2,1     2,2     2,3
#       3,0     3,1     3,2     3,3
# 