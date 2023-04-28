# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        for num in nums:
            if num + 1 in seen:
                continue
            length = 1
            while num - length in seen:
                length += 1
            max_len = max(length, max_len)
        return max_len

nums = [0,3,7,2,5,8,4,6,0,1]
sol = Solution()
print(sol.longestConsecutive(nums))
