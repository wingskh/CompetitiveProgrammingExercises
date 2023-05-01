# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        left_max = 0
        right_max = 0
        left_pos = 0
        right_pos = 0
        max_area = 0

        while left_index < right_index:
            if height[left_index] > left_max:
                left_pos = left_index
                left_max = height[left_index]

            if height[right_index] > right_max:
                right_pos = right_index
                right_max = height[right_index]
            
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1
            
            max_area = max(min(left_max, right_max) * (right_pos - left_pos), max_area)

        return max_area

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))
