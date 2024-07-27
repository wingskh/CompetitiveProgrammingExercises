# https://leetcode.com/problems/hand-of-straights/\
from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_parenthesis_min_count = left_parenthesis_max_count = 0

        for c in s:
            if c == "(":
                left_parenthesis_min_count += 1
                left_parenthesis_max_count += 1
            elif c == "*":
                left_parenthesis_min_count -= 1
                left_parenthesis_max_count += 1
            else:
                left_parenthesis_min_count -= 1
                left_parenthesis_max_count -= 1

            left_parenthesis_min_count = max(left_parenthesis_min_count, 0)
            if left_parenthesis_max_count < 0:
                return False

        return left_parenthesis_min_count == 0


s = "()"
# Output: true
s = "(*))"
# Output: true
sol = Solution()
print(sol.checkValidString(s))
