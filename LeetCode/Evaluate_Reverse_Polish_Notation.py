# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(num1, num2, operand):
            if operand == '+':
                return num1 + num2
            elif operand == '-':
                return num1 - num2
            elif operand == '*':
                return num1 * num2
            elif operand == '/':
                return num1 / num2
            return None
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = calculate(num1, num2, token)
                stack.append(int(result))
        return stack.pop()


tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["18"]
sol = Solution()
print(sol.evalRPN(tokens))
