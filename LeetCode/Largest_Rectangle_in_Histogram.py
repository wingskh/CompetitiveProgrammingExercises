# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = []

        for index in range(len(heights)):
            startHeight = index
            while len(stack) > 0 and stack[-1][1] > heights[index]:
                startHeight, height = stack.pop()
                max_area = max(max_area, (index - startHeight) * height)
            stack.append((startHeight, heights[index]))
        return max_area
    

heights = [1, 3, 2, 1, 2]
# heights = [2, 1, 5, 6, 2, 3]
sol = Solution()
print(sol.largestRectangleArea(heights))
