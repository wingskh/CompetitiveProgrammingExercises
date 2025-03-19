# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, combination):
            new_combination = tuple(combination + (nums[index],))
            next_index = index + 1
            result.add(combination)
            result.add(new_combination)
            if next_index < candidates_len:
                dfs(next_index, new_combination)
                dfs(next_index, combination)

        candidates_len = len(nums)
        result = set((tuple(),))
        nums.sort()
        for index in range(candidates_len):
            dfs(index, tuple())
        return result


nums = [1, 2, 2]
# Output = [[],[1],[1,2],[1,2,2],[2],[2,2]]
nums = [4, 4, 4, 1, 4]
# Output = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
sol = Solution()
print(sol.subsetsWithDup(nums))
