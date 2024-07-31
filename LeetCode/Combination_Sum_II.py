# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def enlarge_combination(index, remaining, combination):
            new_remaining = remaining - candidates[index]
            new_combination = tuple(combination + (candidates[index],))

            if new_remaining == 0:
                if new_combination not in result:
                    result.add(new_combination)
                return
            elif new_remaining < 0:
                return

            next_index = index + 1
            if next_index < candidates_len:
                if new_combination not in seen:
                    seen.add(new_combination)
                    enlarge_combination(next_index, new_remaining, new_combination)
                enlarge_combination(next_index, remaining, combination)

        candidates_len = len(candidates)
        result = set()
        seen = set()
        candidates.sort()
        for index in range(candidates_len):
            if candidates[index] > target:
                break
            enlarge_combination(index, target, tuple())
        return result


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
candidates = [2, 4, 1, 5, 5, 4, 1, 2, 4]
target = 10
# Output: [[1,1,2,2,4],[1,1,4,4],[1,2,2,5],[1,4,5],[2,4,4],[5,5]]
sol = Solution()
print(sol.combinationSum2(candidates, target))
