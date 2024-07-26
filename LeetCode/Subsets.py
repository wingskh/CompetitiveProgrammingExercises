# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possible_subsets = [[]]
        for num in nums:
            i = 0
            possible_subsets_len = len(possible_subsets)
            while i < possible_subsets_len:
                possible_subsets.append(possible_subsets[i] + [num])
                i += 1

        return possible_subsets


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))
