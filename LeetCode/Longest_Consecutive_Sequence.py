# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List, int

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        connection_dict = {}


nums = [0,3,7,2,5,8,4,6,0,1]
sol = Solution(nums)
print(sol.longestConsecutive(nums))


[100,4,200,1,3,2]

# 100   ->      4
# 
# 
# 
# 
# 