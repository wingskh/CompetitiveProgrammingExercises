# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        cur_max = 0
        num_of_jump = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_max:
                num_of_jump += 1
                cur_max = farthest

        return num_of_jump


nums = [2, 3, 1, 1, 4]
# Output: 2
# nums = [2, 3, 0, 1, 4]
# Output: 2
# nums = [0]
# Output: 0
sol = Solution()
print(sol.jump(nums))
