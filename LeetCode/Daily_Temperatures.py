# https://leetcode.com/problems/daily-temperatures/ 
from typing import List
import math

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(math.inf, -1)]
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while temperature > stack[-1][0]:
                _, prev_index = stack.pop()
                result[prev_index] = index - prev_index
            stack.append((temperature, index))
        return result

temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]
sol = Solution()
print(sol.dailyTemperatures(temperatures))



# 73, 74, 75, 71, 69, 72, 76, 73
# 74  75  76  72  72  76  0   0


# 74 75
# 75 71 69 72