# https://leetcode.com/problems/target-sum/
class Solution:
    # Dynamic Programming
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        max_sum = sum(nums)
        max_range = max_sum * 2 + 1
        target = abs(target)
        if max_sum < target or (target + sum(nums)) % 2 != 0:
            return 0

        dp = [[0] * max_range for _ in range(nums_length)]
        dp[0][max_sum + nums[0]] += 1
        dp[0][max_sum - nums[0]] += 1

        for i in range(1, nums_length):
            for s in range(max_range):
                # left side
                if s - nums[i] >= 0 and dp[i - 1][s - nums[i]] > 0:
                    dp[i][s] += dp[i - 1][s - nums[i]]

                # right side
                if s + nums[i] <= max_range - 1 and dp[i - 1][s + nums[i]] > 0:

                    dp[i][s] += dp[i - 1][s + nums[i]]

        return dp[-1][max_sum + target]

    # Find all combination using dict
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last_round_comb = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {nums[0]: 2}
        nums_length = len(nums)

        for i in range(1, nums_length):
            cur_round_comb = {}
            for s in last_round_comb:
                if s - nums[i] not in cur_round_comb:
                    cur_round_comb[s - nums[i]] = 0

                if s + nums[i] not in cur_round_comb:
                    cur_round_comb[s + nums[i]] = 0

                cur_round_comb[s - nums[i]] += last_round_comb[s]
                cur_round_comb[s + nums[i]] += last_round_comb[s]
            last_round_comb = cur_round_comb

        return last_round_comb[target] if target in last_round_comb else 0
