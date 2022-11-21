# https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = result = nums[0] 
        for i in range(1, len(nums)):
            max_sum = max(max_sum, 0) + nums[i]
            result = max(max_sum, result)
        return result


nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)
