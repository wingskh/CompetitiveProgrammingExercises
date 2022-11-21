# https://leetcode.com/problems/basic-calculator/
import re

class Solution:
    def calculate(self, s: str) -> int:
        def cal(eq):
            operators = ["+", "-"]
            eq = eq.replace("--", "+").replace("-+", "-").replace("+-", "-")
            nums = re.split('[\+|-]', eq)
            operators = re.findall('[+-]', eq)
            result = 0

            while len(nums) != 0:
                num = nums.pop()
                if num != "":
                    num = int(num)
                    operator = operators.pop() if len(operators) != 0 else "+"
                    if operator == "+":
                        result += num
                    else:
                        result -= num
                else:
                    break
            return result
        
        s = s.replace(" ", "")
        while True:
            if "(" in s:
                left_bracket = s.rindex("(")
                right_bracket = left_bracket + s[left_bracket+1:].index(")") + 1
                s = s[:left_bracket] + str(cal(s[left_bracket + 1:right_bracket])) + s[right_bracket + 1:]
            else:
                return cal(s)

s = "(1+(4+5+2)-3)+(6+8)"
sol = Solution()
result = sol.calculate(s)
print(result)
