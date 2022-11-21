# https://leetcode.com/problems/valid-parentheses/
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        if len(s) % 2 != 0 or s[0] not in bracket_pairs:
            return False
            
        for chr in s:
            if chr in [')',  '}', ']']:
                if len(stack) == 0 or bracket_pairs[chr] != stack.pop():
                    return False
            else:
                stack.append(chr)
        return len(stack) == 0

s = "(("
sol = Solution()
result = sol.isValid(s)
print(result)
