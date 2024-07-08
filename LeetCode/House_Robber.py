# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums) + 2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i]+nums[i], dp[i+1])
        
        return dp[-1]


nums = [1,2,3,1]
# Output: 4
sol = Solution()
print(sol.rob(nums))
