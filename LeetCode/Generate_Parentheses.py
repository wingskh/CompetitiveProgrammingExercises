# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(string, left_parentheses_count, right_parentheses_count):
            if right_parentheses_count == n:
                result.append(string)
            else:
                if left_parentheses_count < n:
                    dfs(string + '(', left_parentheses_count + 1 , right_parentheses_count)
                if right_parentheses_count < left_parentheses_count:
                    dfs(string + ')', left_parentheses_count, right_parentheses_count + 1)

        result = []
        dfs('', 0 , 0)
        return result

n = 3
sol = Solution()
print(sol.generateParenthesis(n))
