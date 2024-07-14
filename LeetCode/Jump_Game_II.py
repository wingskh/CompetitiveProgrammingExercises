# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        farthest_jump = nums[0]
        last_jump_limit = 0
        num_of_jump = 0

        for i in range(len(nums) - 1):
            farthest_jump = max(farthest_jump, i + nums[i])
            if i == last_jump_limit:
                num_of_jump += 1
                last_jump_limit = farthest_jump

        return num_of_jump


nums = [2, 3, 1, 1, 4]
# Output: 2
# nums = [2, 3, 0, 1, 4]
# Output: 2
# nums = [0]
# Output: 0
sol = Solution()
print(sol.jump(nums))
