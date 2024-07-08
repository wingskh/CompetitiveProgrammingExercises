# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_next_length = 0
        for num in nums:
            if max_next_length < 0:
                return False
            elif num > max_next_length:
                max_next_length = num
            max_next_length -= 1

        return True


nums = [2, 3, 1, 1, 4]
# Output: true
nums = [3, 2, 1, 0, 4]
# Output: false
sol = Solution()
print(sol.canJump(nums))
