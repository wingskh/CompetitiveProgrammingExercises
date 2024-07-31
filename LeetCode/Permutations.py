# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(chosen_nums):
            if len(chosen_nums) == len(nums):
                result.append([nums[i] for i in chosen_nums])
                return

            for i in range(len(nums)):
                if i not in chosen_nums:
                    dfs(chosen_nums + [i])

        result = []
        for i in range(len(nums)):
            dfs([i])

        return result


nums = [1,2,3]
# Output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
sol = Solution()
print(sol.permute(nums))
