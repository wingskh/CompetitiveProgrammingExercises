# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        total_number_in_a_set = numRows * 2 - 2
        if numRows == 1:
            return s
        result = ""

        for row in range(numRows):
            i = row
            flipped = True
            diff = row * 2
            need_flip = row != 0 and row != numRows - 1
            while i < len(s):
                if row == 3:
                    print(i)
                result += s[i]
                if need_flip:
                    if flipped:
                        i += (numRows - 1 - row) * 2
                    else:
                        i += diff
                    flipped = not flipped
                else:
                    i += total_number_in_a_set

        return result
