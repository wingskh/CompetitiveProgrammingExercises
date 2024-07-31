# https://leetcode.com/problems/combination-sum/
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate_index, total_sum, chosen_candidate):
            if total_sum == target:
                result.append(chosen_candidate)
                return
            elif total_sum > target or candidate_index == len(candidates):
                return

            dfs(
                candidate_index,
                total_sum + candidates[candidate_index],
                chosen_candidate + [candidates[candidate_index]],
            )
            dfs(candidate_index + 1, total_sum, chosen_candidate)

        result = []
        dfs(0, 0, [])
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def enlarge_combination(index, remaining, combination):
            new_remaining = remaining - candidates[index]
            new_combination = tuple(combination + (candidates[index], ))

            if new_remaining == 0:
                if new_combination not in result:
                    result.add(new_combination)
                return
            elif new_remaining < 0:
                return
            
            enlarge_combination(index, new_remaining, new_combination)
            next_index = index + 1
            if next_index < candidates_len:
                enlarge_combination(next_index, remaining, combination)

        candidates_len = len(candidates)
        result = set()
        candidates.sort()
        for index in range(candidates_len):
            enlarge_combination(index, target, tuple())
        return result


candidates = [2,3,6,7]
target = 7
# Output: [[2,2,3],[7]]
# candidates = [3,5,8]
# target = 11
# [[3,3,5],[3,8]]
candidates = [8,7,4,3]
target = 11
# Output: [[8,3],[7,4],[4,4,3]]
sol = Solution()
print(sol.combinationSum(candidates, target))