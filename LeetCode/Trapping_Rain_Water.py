# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water_volumn = 0
        left_prev_height = 0
        left_temp_water_volumn = 0
        right_temp_water_volumn = 0
        right_prev_height = 0
        height_len = len(height)

        for i in range(height_len):
            if height[i] >= left_prev_height:
                left_prev_height = height[i]
                water_volumn += left_temp_water_volumn
                left_temp_water_volumn = 0
            else:
                left_temp_water_volumn += left_prev_height - height[i]

            if height[height_len - i - 1] > right_prev_height:
                right_prev_height = height[height_len - i - 1]
                water_volumn += right_temp_water_volumn
                right_temp_water_volumn = 0
            else:
                right_temp_water_volumn += right_prev_height - height[height_len - i - 1]

        return water_volumn

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
