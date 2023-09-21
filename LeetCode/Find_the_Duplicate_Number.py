# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# nums = [1,3,4,2,2]
# Output: 2
# nums = [3,1,3,4,2]
# Output: 3
# nums = [2,1,2]
# Output: 2
# nums = [4,3,1,4,2]
# Output: 4
# nums = [1,3,4,2,1]
# Output: 1
nums = [2,5,9,6,9,3,8,9,7,1]
# Output: 9

sol = Solution()
result = sol.findDuplicate(nums)
print(result)

nums = [3,1,3,4,2]
