# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate_index, total_sum, chosen_candidate):
            nonlocal candidates, target, result
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
        candidates.sort(reverse=True)
        dfs(0, 0, [])
        return result
